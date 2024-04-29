#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: github_repo_info.py
@date: 2024/4/28 
"""
from datetime import datetime, timedelta

from common.logger import log
from utils.request_utils import RequestUtil


def get_github_repo_info(repo_names, token):
    results = []
    headers = {'Authorization': f'token {token}'}
    for repo_name in repo_names:
        url = f"{repo_name}"
        while True:

            # Make a GET request to the GitHub API with authentication headers
            response = RequestUtil('base', 'url').send_request("get", url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                break
            elif response.status_code == 202:
                # Retry if status code is 202
                continue
            else:
                log.error(
                    f"Failed to fetch data from GitHub API for repository: {repo_name}. Status code: {response.status_code}")
                break

        # Convert the response to JSON format
        repo_info = response.json()

        # Extract the desired information
        stars = repo_info['stargazers_count']
        forks = repo_info['forks_count']

        # Fetch contributors insights for the repository
        insights_url = f"{repo_name}/stats/contributors"

        while True:
            insights_response = RequestUtil('base', 'url').send_request("get", insights_url, headers=headers)

            # Check if the request was successful (status code 200)
            if insights_response.status_code == 200:
                break
            elif insights_response.status_code == 202:
                # Retry if status code is 202
                continue
            else:
                log.error(
                    f"Failed to fetch insights data from GitHub API for repository: {repo_name}. Status code: {insights_response.status_code}")
                break

        insights_data = insights_response.json()

        # Calculate total community engagement and engagement in the last six months
        total_community_engagement = 0
        six_months_ago = datetime.now() - timedelta(days=30 * 6)
        six_months_community_engagement = 0
        contributors_count = len(insights_data)
        for contributor in insights_data:
            for week in contributor['weeks']:
                total_community_engagement += week['c']
                week_date = datetime.utcfromtimestamp(week['w'])
                if week_date >= six_months_ago:
                    six_months_community_engagement += week['c']
        log.info("%s  完成 基本信息扫描", repo_name)
        # Append the extracted information to results
        results.append(
            (repo_name, stars, forks, total_community_engagement, six_months_community_engagement, contributors_count))

    return results
