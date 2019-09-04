## Branching

### Branch

List, create, or delete branches. <br>
https://git-scm.com/docs/git-branch <br>
`branch`

> [Create a remote branch](https://stackoverflow.com/questions/1519006/how-do-you-create-a-remote-git-branch) <br>
git checkout -b <feature_branch_name> <br>
git push -u <br>
git push --set-upstream origin <br> <feature_branch_name>

> Pull / Copy a remote branch
https://gist.github.com/fabianmoronzirfas/4023446 <br>
https://stackoverflow.com/questions/9537392/git-fetch-remote-branch <br>
git fetch <br>
git checkout --track origin/<remote_branch_name>

> Git Visual Branch Changes
https://stackoverflow.com/questions/1057564/pretty-git-branch-graphs <br>
git log --graph --oneline --all

Local branches in your repository <br>
`git branch`

Remote branches in repository <br>
`git branch -a`

Delete Branch. <br>
`git branch -d 'branch_name'`

Delete unmerged Branche. <br>
`git branch -D 'branch_name'`

Rename branch a branch while pointed to any branch. <br>
`git branch -m 'old_name' 'new_name'`

Rename the current branch. <br>
`git branch -m 'newname'`

Only list branches merged branches. <br>
`git branch --merged`

Only list unmerged branches. <br>
`git branch --no-merged`