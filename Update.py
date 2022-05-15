# TOM_CORE version n. 0.1.5
# Copyright (C) 2022 Tomáš Sýkora

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, is available on:
# https://www.solvethat.net/installer/GNU_License.pdf

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

# 2. Install requirements.txt with local pip Filename: "{app}\venv\Scripts\pip.exe"; Parameters:"install -r {app}\install_assets\requirements.txt"; Flags: runasoriginaluser runhidden
os.system(repo_path + '\\venv\\Scripts\\pip.exe install -r ' + repo_path + '\\install_assets\\requirements.txt')
