import os


def get_git_head_info():
  import git  # GitPython
  try:
    path = os.getcwd()
    repo = git.Repo(path)
    sha = repo.head.commit.hexsha
    return " ".join(list(repo.remote().urls) + [sha])
  except Exception as e:
    print('error while inferring git path : {}'.format(e))
    return ""
