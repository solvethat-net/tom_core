import os
import git

# Script for app update with git
# 1. Check if .git dir exist, when does than do pull or do init when doesn't

repo_path = os.path.dirname(os.path.abspath(__file__))
if os.path.isdir(repo_path + '\\.git'):
    empty_repo = git.Repo(repo_path)
    origin = empty_repo.remote('origin')
    origin.pull()
else:
    empty_repo = git.Repo.init(os.path.join(repo_path))
    origin = empty_repo.create_remote('origin', 'https://github.com/solvethat-net/tom_core.git')
    assert origin.exists()
    assert origin == empty_repo.remotes.origin == empty_repo.remotes['origin']
    origin.fetch()
    empty_repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()

# 2. Install requirements.txt with local pip
os.system(repo_path + '\\venv\\Scripts\\pip.exe install -r ' + repo_path + '\\install_assets\\requirements.txt')
