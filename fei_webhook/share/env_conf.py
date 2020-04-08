"""从环境变量获取一些私有的配置信息
    # for database
    export env_db_host=
    export env_db_database=
    export env_db_port=
    export env_db_user=
    export env_db_password=

    # for github webhook
    export github_hook_script = 
    export github_sec_code = 

    # for local gitserver-2223 (dockerized)  webhook
    export hhxx_hook_script = 
    export hhxx_sec_code = 
"""

import os

class WebhookConfig:
    github_hook_script = os.environ.get('github_hook_script')
    github_sec_code = str(os.environ.get('github_sec_code'))

    hhxx_hook_script = os.environ.get('hhxx_hook_script')
    hhxx_sec_code = str(os.environ.get('hhxx_sec_code'))

    github_hook_script_fei = os.environ.get('github_hook_script_fei')
    github_sec_code_fei = os.environ.get('github_sec_code_fei')
