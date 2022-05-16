# TOM_CORE version n. 0.1.6
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
# https://www.solvethat.net/installer/LICENSE

import os
import sys

from dulwich import porcelain

# Check if .git dir exist, when does than do pull or do init when doesn't
# After running this script is recommended to run pip install -r requirements.txt
if __name__ == "__main__":
    # First arg is for install dir path, argument is obligatory
    print("Update via GIT script")
    remote_repo = "https://github.com/solvethat-net/tom_core.git"
    repo_path = sys.argv[1]
    if os.path.isdir(repo_path + '\\.git'):
        print("Pull repository", repo_path)
        porcelain.pull(repo_path)
    else:
        print("Clone repository", repo_path)
        porcelain.clone(remote_repo, repo_path)
