# Git

- Configurations
- Staging
- Commit
- Branch

## Configuration

#### Config
Set Login, password for git. <br>
`git config --global user.email "you@example.com"` <br>
`git config --global user.name "Your Name"` <br>
`git config --global user.password "your password"`

Reset credentials. <br>
https://stackoverflow.com/questions/15381198/remove-credentials-from-git <br>
`git config --global --unset credential.helper`

***

#### Init
Create an empty Git repository or reinitialize an existing one. <br>
https://git-scm.com/docs/git-init <br>
`git init`

***

#### Clone
Clone a repository into a new directory. <br>
https://git-scm.com/docs/git-clone <br>
`git clone 'Repository URL'`

***

## Changes status

#### Status

Show the working tree status. <br>
https://git-scm.com/docs/git-status <br>
`git status`

#### Fetch

Check the remote changes. <br>
`git fetch`

***

#### Add

Add file contents to the index. <br>
https://git-scm.com/docs/git-add <br>
`git add 'file_name'`

Stages all changes. <br>
`git add -A`  

Stages new files and modifications, without deletions. <br>
`git add .` 

Stages modifications and deletions, without new files. <br>
`git add -u` 

 Interactive mode for details. <br>
 https://git-scm.com/book/en/v2/Git-Tools-Interactive-Staging <br>
 `git add -i`

***

## Files

Copy all modified and new files to upper directory <br>
`cp --parents $(git ls-files --modified --others) ../`

#### Remove Files

Remove files from the working tree and from the index. <br>
https://git-scm.com/docs/git-rm <br>
`git rm 'file_name'`

Remove from repository keep local <br>
`git rm --cached <file>`

***

#### Commit

Record changes to the repository. <br>
https://git-scm.com/docs/git-commit <br>
`git commit`

> [_Undo the last commit_](https://www.git-tower.com/learn/git/faq/undo-last-commit) <br>
`git reset --soft HEAD~1`

>Add all modified and deleted, use msg for commit message. <br>
`git commit -am "msg"`

>Squash two commits into one. <br>
`git reset --soft "HEAD^"` <br>
`git commit --amend`

Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected. <br>
`git commit -a`

Use the given "msg" as the commit message. <br>
`git commit -m "msg"`

Convenient way to modify the most recent commit. It can also be used to simply edit the previous commit message without changing its snapshot. <br>
`git commit --amend`

***

## Branching

#### Branch

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

***

#### Rebase
Reapply commits on top of another base tip. <br>
https://git-scm.com/docs/git-rebase <br>
https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase <br>
`git rebase`

***

#### Merge
Join two or more development histories together. <br>
https://git-scm.com/docs/git-merge <br>
`git merge`

> Merge two local branches <br>
`git checkout -b hotfix` <br>
`git commit -am "hot fix"` <br>
`git checkout master` <br>
`git merge hotfix`

***

#### Checkout

Switch branches or restore working tree files. <br>
https://git-scm.com/docs/git-checkout <br>
`git checkout 'branch_name'`

> Create new dranch and switch to It <br>
`git checkout -b 'new_branch_name'`

***

#### Push

Update remote refs along with associated objects. <br>
https://git-scm.com/docs/git-push <br>
`git push`

***

#### Log
Show commit logs. <br>
https://git-scm.com/docs/git-log <br>
`git log`

***

#### Show
Show various types of objects. <br>
https://git-scm.com/docs/git-show <br>
`git show`

***

#### Rest
Reset current HEAD to the specified state <br>
https://git-scm.com/docs/git-reset <br>
`git reset` 

***

#### Stash
Stash the changes in a dirty working directory away. <br>
https://git-scm.com/docs/git-stash <br>
`git stash`

Rever changes from stash <br>
`git stash pop`

***

#### Pull
Fetch from and integrate with another repository or a local branch. <br>
https://git-scm.com/docs/git-pull <br>
`git pull`

***