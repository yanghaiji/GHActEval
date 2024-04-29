from act_eval.al import al
from utils.load_yaml import read_config

if __name__ == '__main__':
    repo_names = read_config("repos", "/config/application.yaml")
    # Replace with your GitHub Personal Access Token
    github_token = read_config("github_token", "/config/application.yaml")

    al(repo_names, github_token)
