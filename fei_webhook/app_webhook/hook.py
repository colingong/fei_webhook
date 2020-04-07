"""一个webhook的执行"""
from share.env_conf import WebhookConfig
from .models import WebhookLog
import subprocess
import json
from abc import ABC, abstractmethod
import hmac, hashlib

class WebhookSourceNotValid(Exception):
    pass

class WebHook(ABC):
    """接受一个请求，然后将必须的几个属性赋值
    log = WebHook()
    <...验证是否允许的来源...> self.verified = True
    log.set_log_fields()                从self.data_dict里取值
    log.from_site = ...                 无法set_log_fields的项，手动赋值一遍
    log.shell_script = '<执行的命令>'
    log.save_log() :这样就执行脚本并且保存日志
    必须的属性包括：
       from_site: 需要知道这个请求来自于何处
       shell_script: 需要知道收到请求后去执行哪个脚本
       verified: 需要先赋值为True才会保存；验证需要自行处理，因为每个webhook的验证方式不一样
                 可以考虑post过来的json包括一个{"sec": sec_code}，然后每次验证它
    
    Arguments:
        object {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    def __init__(self, request, sec_code=None):
        self.sec_code = sec_code
        self.request = request
        self.shell_script = ''
        self.data_dict = self.convert_data_to_dict()
        self.webhooklog = self.gen_webhooklog()

        self._empty_dict = {"no_key": "no_value"}
        self.verified = self._if_valid_source()
    
    @abstractmethod
    def _if_valid_source(self):
        raise Exception("需要实现验证，确认是否合法来源")

    @abstractmethod
    def set_fields(self):
        raise Exception('需要给webhooklog的字段赋值')

    def convert_data_to_dict(self):
        """处理get或post请求，获取有用的数据"""
        if self.request.method == 'GET':
            data = dict(self.request.GET)
        elif self.request.method == 'POST':
            data = json.loads(self.request.body)
        else:
            return None
        return data
    
    def gen_webhooklog(self):
        """获取日志各字段的值"""

        webhooklog = WebhookLog()
        return webhooklog

    def save_log(self):
        print(f'verified ===> {self.verified}')
        if self.verified:
            self.set_fields()
            output = self._run_shell_script()
            self.webhooklog.save()
            return output

        return None

    def _run_shell_script(self):
        try:
            output = subprocess.check_output([self.shell_script, ])
            return output
        except:
            print(f'script run error ---> {self.shell_script}')


class GithubHook(WebHook):

    def set_fields(self):
        self.webhooklog.from_site = 'Github.com'

        self.webhooklog.ref = self.data_dict.get("ref", '')
        self.webhooklog.before = self.data_dict.get("before", '')
        self.webhooklog.after = self.data_dict.get("after", '')
        repository = self.data_dict.get("repository", self._empty_dict)
        head_commit = self.data_dict.get("head_commit", self._empty_dict)
        self.webhooklog.repo_name = repository.get("full_name", '')
        self.webhooklog.html_url = repository.get("html_url", '')
        self.webhooklog.hooks_url = repository.get("hooks_url", '')
        self.webhooklog.commit_message = head_commit.get("message", '')
        print(f'---> set_fields done')

    def _if_valid_source(self):
        sign_from_github = self.request.headers.get('X-Hub-Signature').split('=')[1]
        raw = self.request.body
        print(raw)
        key = self.sec_code.encode('utf-8')

        hashed = hmac.new(key, raw, hashlib.sha1)
        sign = hashed.hexdigest()
        print(f'github sign: {sign_from_github} / local check sign: {sign}')
        
        # 给测试用的sec_code，从环境变量获取
        test_sign = str(self.data_dict.get('sec_code', ''))

        if sign_from_github == sign or test_sign == self.sec_code:
            return True
        
        return False

class HhxxGitHook(WebHook):
    """用于接受本地git server 在post-receive发过来的请求
    curl -H "Content-Type:application/json" -X POST -d '{"sec_code":""}' <http://site/...>
    """
    def set_fields(self):
        self.webhooklog.from_site = "hhxx git server"
        self.webhooklog.after = self.data_dict.get("after", '')

    def _if_valid_source(self):
        my_code = str(self.data_dict.get('sec_code'))
        if my_code == self.sec_code:
            return True

        return False
        