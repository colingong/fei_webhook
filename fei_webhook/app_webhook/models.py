"""GithubLog: 记录github的webhook
    # 都是github webhook里的数据
    ref =
    before = 
    after = 

    # "repository":{"full_name": ...}
    repo_name = 

    # "repository":{"html_url": ...}
    html_url = 

    # "repository":{"hooks_url": ...}
    hooks_url = 
"""

from django.db import models

# Create your models here.

class GithubLog(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    ref = models.CharField(max_length=200, blank=True)
    before = models.CharField(max_length=50, blank=True)
    after = models.CharField(max_length=50, blank=True)

    # "repository":{"full_name": ...}
    repo_name = models.CharField(max_length=1000, blank=True)

    # "repository":{"html_url": ...}
    html_url = models.URLField(max_length=1000, blank=True)

    # "repository":{"hooks_url": ...}
    hooks_url = models.URLField(max_length=1000, blank=True)

    # commits: {message: ... }
    commit_message = models.CharField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.repo_name
