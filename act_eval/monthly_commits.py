#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: monthly_commits.py
@date: 2024/4/28 
"""
from datetime import datetime, timedelta

from common.logger import log
from utils.request_utils import RequestUtil


def get_monthly_commits(repo_name, token):
    headers = {'Authorization': f'token {token}'}
    commits_url = f"{repo_name}/stats/commit_activity"
    response = RequestUtil('base', 'url').send_request("GET", commits_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        commit_counts = [week['total'] for week in data]

        # Aggregate weekly commits into monthly
        monthly_commits = {}
        current_date = datetime.now()
        for i in range(12):
            last_month = current_date - timedelta(days=30 * i)
            month_name = last_month.strftime('%Y-%m')
            monthly_commits[month_name] = sum(commit_counts[i * 4:(i + 1) * 4])

        log.info("%s 完成 月份分析", repo_name)
        return monthly_commits
    else:

        log.error(
            f"Failed to fetch commit activity data from GitHub API for repository: {repo_name}. Status code: {response.status_code}")
        return None
