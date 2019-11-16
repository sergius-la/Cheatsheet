# Git

- __[Configurations:](/git/config.md)__
  - `config`
- __[Staging:](/git/stage.md)__
  - `commit:` reset commit, edit commit, squash
- [**Branching:**](/git/branching.md) `branch`
  - remote
  - local

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


> Git Visual Branch Changes
https://stackoverflow.com/questions/1057564/pretty-git-branch-graphs <br>
git log --graph --oneline --all

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

- Resources:
  - [_Most commonly used git tips and tricks_](https://github.com/git-tips/tips)