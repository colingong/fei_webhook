import hashlib, hmac

github_data = '''{
  "ref": "refs/heads/master",
  "before": "458f00c5d4f50861a560a82540f5c74ab46eb1f1",
  "after": "0109cf998c3acc18e400e0be1e69610eff2bd233",
  "repository": {
    "id": 252496642,
    "node_id": "MDEwOlJlcG9zaXRvcnkyNTI0OTY2NDI=",
    "name": "fei_webhook",
    "full_name": "colingong/fei_webhook",
    "private": false,
    "owner": {
      "name": "colingong",
      "email": "colingong@hotmail.com",
      "login": "colingong",
      "id": 11820591,
      "node_id": "MDQ6VXNlcjExODIwNTkx",
      "avatar_url": "https://avatars2.githubusercontent.com/u/11820591?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/colingong",
      "html_url": "https://github.com/colingong",
      "followers_url": "https://api.github.com/users/colingong/followers",
      "following_url": "https://api.github.com/users/colingong/following{/other_user}",
      "gists_url": "https://api.github.com/users/colingong/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/colingong/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/colingong/subscriptions",
      "organizations_url": "https://api.github.com/users/colingong/orgs",
      "repos_url": "https://api.github.com/users/colingong/repos",
      "events_url": "https://api.github.com/users/colingong/events{/privacy}",
      "received_events_url": "https://api.github.com/users/colingong/received_events",
      "type": "User",
      "site_admin": false
    },
    "html_url": "https://github.com/colingong/fei_webhook",
    "description": "Listen webhook then start some task on local ECS host.",
    "fork": false,
    "url": "https://github.com/colingong/fei_webhook",
    "forks_url": "https://api.github.com/repos/colingong/fei_webhook/forks",
    "keys_url": "https://api.github.com/repos/colingong/fei_webhook/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/colingong/fei_webhook/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/colingong/fei_webhook/teams",
    "hooks_url": "https://api.github.com/repos/colingong/fei_webhook/hooks",
    "issue_events_url": "https://api.github.com/repos/colingong/fei_webhook/issues/events{/number}",
    "events_url": "https://api.github.com/repos/colingong/fei_webhook/events",
    "assignees_url": "https://api.github.com/repos/colingong/fei_webhook/assignees{/user}",
    "branches_url": "https://api.github.com/repos/colingong/fei_webhook/branches{/branch}",
    "tags_url": "https://api.github.com/repos/colingong/fei_webhook/tags",
    "blobs_url": "https://api.github.com/repos/colingong/fei_webhook/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/colingong/fei_webhook/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/colingong/fei_webhook/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/colingong/fei_webhook/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/colingong/fei_webhook/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/colingong/fei_webhook/languages",
    "stargazers_url": "https://api.github.com/repos/colingong/fei_webhook/stargazers",
    "contributors_url": "https://api.github.com/repos/colingong/fei_webhook/contributors",
    "subscribers_url": "https://api.github.com/repos/colingong/fei_webhook/subscribers",
    "subscription_url": "https://api.github.com/repos/colingong/fei_webhook/subscription",
    "commits_url": "https://api.github.com/repos/colingong/fei_webhook/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/colingong/fei_webhook/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/colingong/fei_webhook/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/colingong/fei_webhook/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/colingong/fei_webhook/contents/{+path}",
    "compare_url": "https://api.github.com/repos/colingong/fei_webhook/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/colingong/fei_webhook/merges",
    "archive_url": "https://api.github.com/repos/colingong/fei_webhook/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/colingong/fei_webhook/downloads",
    "issues_url": "https://api.github.com/repos/colingong/fei_webhook/issues{/number}",
    "pulls_url": "https://api.github.com/repos/colingong/fei_webhook/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/colingong/fei_webhook/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/colingong/fei_webhook/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/colingong/fei_webhook/labels{/name}",
    "releases_url": "https://api.github.com/repos/colingong/fei_webhook/releases{/id}",
    "deployments_url": "https://api.github.com/repos/colingong/fei_webhook/deployments",
    "created_at": 1585841942,
    "updated_at": "2020-04-07T07:55:33Z",
    "pushed_at": 1586246213,
    "git_url": "git://github.com/colingong/fei_webhook.git",
    "ssh_url": "git@github.com:colingong/fei_webhook.git",
    "clone_url": "https://github.com/colingong/fei_webhook.git",
    "svn_url": "https://github.com/colingong/fei_webhook",
    "homepage": null,
    "size": 63,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "forks_count": 0,
    "mirror_url": null,
    "archived": false,
    "disabled": false,
    "open_issues_count": 0,
    "license": {
      "key": "apache-2.0",
      "name": "Apache License 2.0",
      "spdx_id": "Apache-2.0",
      "url": "https://api.github.com/licenses/apache-2.0",
      "node_id": "MDc6TGljZW5zZTI="
    },
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "master",
    "stargazers": 0,
    "master_branch": "master"
  },
  "pusher": {
    "name": "colingong",
    "email": "colingong@hotmail.com"
  },
  "sender": {
    "login": "colingong",
    "id": 11820591,
    "node_id": "MDQ6VXNlcjExODIwNTkx",
    "avatar_url": "https://avatars2.githubusercontent.com/u/11820591?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/colingong",
    "html_url": "https://github.com/colingong",
    "followers_url": "https://api.github.com/users/colingong/followers",
    "following_url": "https://api.github.com/users/colingong/following{/other_user}",
    "gists_url": "https://api.github.com/users/colingong/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/colingong/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/colingong/subscriptions",
    "organizations_url": "https://api.github.com/users/colingong/orgs",
    "repos_url": "https://api.github.com/users/colingong/repos",
    "events_url": "https://api.github.com/users/colingong/events{/privacy}",
    "received_events_url": "https://api.github.com/users/colingong/received_events",
    "type": "User",
    "site_admin": false
  },
  "created": false,
  "deleted": false,
  "forced": false,
  "base_ref": null,
  "compare": "https://github.com/colingong/fei_webhook/compare/458f00c5d4f5...0109cf998c3a",
  "commits": [
    {
      "id": "0109cf998c3acc18e400e0be1e69610eff2bd233",
      "tree_id": "fe18db4be53eb43dbf10b3130ec028b56193b456",
      "distinct": true,
      "message": "dummy",
      "timestamp": "2020-04-07T15:56:42+08:00",
      "url": "https://github.com/colingong/fei_webhook/commit/0109cf998c3acc18e400e0be1e69610eff2bd233",
      "author": {
        "name": "pf",
        "email": "colingong@hotmail.com",
        "username": "colingong"
      },
      "committer": {
        "name": "pf",
        "email": "colingong@hotmail.com",
        "username": "colingong"
      },
      "added": [

      ],
      "removed": [
        "dummy.txt"
      ],
      "modified": [

      ]
    }
  ],
  "head_commit": {
    "id": "0109cf998c3acc18e400e0be1e69610eff2bd233",
    "tree_id": "fe18db4be53eb43dbf10b3130ec028b56193b456",
    "distinct": true,
    "message": "dummy",
    "timestamp": "2020-04-07T15:56:42+08:00",
    "url": "https://github.com/colingong/fei_webhook/commit/0109cf998c3acc18e400e0be1e69610eff2bd233",
    "author": {
      "name": "pf",
      "email": "colingong@hotmail.com",
      "username": "colingong"
    },
    "committer": {
      "name": "pf",
      "email": "colingong@hotmail.com",
      "username": "colingong"
    },
    "added": [

    ],
    "removed": [
      "dummy.txt"
    ],
    "modified": [

    ]
  }
}'''

github_sign = "X-Hub-Signature: sha1=513173448fbb22285a26e73ae6ba9285212bb400"

import json

# payload = json.dumps(github_data).encode('utf-8')
# payload = json.dumps(github_data)

data_dict = json.loads(github_data)

payload = json.dumps(github_data, separators=(',', ':')).encode('utf-8')
print(payload)

def func1():
    key = '123456'.encode('utf-8')
    raw = payload
    sign = hmac.new(key, raw, hashlib.sha1).hexdigest()
    print(sign, github_sign)

def func2():
    import os

    a = "123456"
    print(a.encode('utf-8'))
    print(b'123456')
    b = 123456
    bb = str(b).encode('utf-8')
    print(f'bytes ---> {bb}')

if __name__ == '__main__':
    func1()
    # func2()

