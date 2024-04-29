#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: al.py
@date: 2024/4/28 
"""
from datetime import datetime

import matplotlib.pyplot as plt

from act_eval.github_repo_info import get_github_repo_info
from act_eval.monthly_commits import get_monthly_commits


def al(repo_names, github_token):
    data = get_github_repo_info(repo_names, github_token)
    if data:
        # Plotting the four dimensions
        fig, axs = plt.subplots(3, 2, figsize=(36, 28))  # Increase the figsize to double the width
        # Adjusting subplot parameters to reduce bottom spacing
        # plt.subplots_adjust(bottom=0.05, hspace=2, wspace=2)
        # Add title to the entire figure
        # fig.suptitle('GitHub Repository Analysis', fontsize=38)
        # Plotting Stars
        axs[0, 0].set_title('Stars')
        for repo_name, stars, _, _, _, _ in data:
            new_repo_name = repo_name.split('/')[1]
            axs[0, 0].bar(new_repo_name, stars, width=0.4, label=f'{new_repo_name}')
        axs[0, 0].set_ylabel('Count')
        axs[0, 0].legend()

        # Plotting Forks
        axs[0, 1].set_title('Forks')
        for repo_name, _, forks, _, _, _ in data:
            new_repo_name = repo_name.split('/')[1]
            axs[0, 1].bar(new_repo_name, forks, width=0.4, label=f'{new_repo_name}')
        axs[0, 1].set_ylabel('Count')
        axs[0, 1].legend()

        # Plotting Total Community Engagement
        axs[1, 0].set_title('Total Community Engagement')
        for repo_name, _, _, total, _, _ in data:
            new_repo_name = repo_name.split('/')[1]
            axs[1, 0].bar(new_repo_name, total, width=0.4, label=f'{new_repo_name}')
        axs[1, 0].set_ylabel('Count')
        axs[1, 0].legend()

        # Plotting Last Six Months Community Engagement
        axs[1, 1].set_title('6-Month Community Engagement Overview')
        for repo_name, _, _, _, six_months, _ in data:
            new_repo_name = repo_name.split('/')[1]
            axs[1, 1].bar(new_repo_name, six_months, width=0.4, label=f'{new_repo_name}')
        axs[1, 1].set_ylabel('Count')
        axs[1, 1].legend()

        # Plotting Contributors Count
        axs[2, 0].set_title('Annual Contributors Overview')
        for repo_name, _, _, _, _, contributors_count in data:
            new_repo_name = repo_name.split('/')[1]
            axs[2, 0].bar(new_repo_name, contributors_count, width=0.4, label=f'{new_repo_name}')
        axs[2, 0].set_ylabel('Count')
        axs[2, 0].legend()

        # Plotting Monthly Commits
        axs[2, 1].set_title('12-Month Commit Summary')
        for repo_name in repo_names:
            monthly_commits = get_monthly_commits(repo_name, github_token)
            if monthly_commits:
                sorted_commits = sorted(monthly_commits.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m'))
                months = [month for month, _ in sorted_commits]
                commit_counts = [count for _, count in sorted_commits]
                new_repo_name = repo_name.split('/')[1]
                axs[2, 1].plot(months, commit_counts, marker='o', linestyle='-', label=f'{new_repo_name}')
        axs[2, 1].set_ylabel('Commit Count')
        axs[2, 1].legend()

        # Hide the last subplot
        # fig.delaxes(axs[3, 0])
        # fig.delaxes(axs[3, 1])

        plt.tight_layout()
        plt.show()
