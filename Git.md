# Git

#### Init
Create an empty Git repository or reinitialize an existing one. <br>
https://git-scm.com/docs/git-init <br>
`git init`

***

#### Clone
Clone a repository into a new directory. <br>
https://git-scm.com/docs/git-clone <br>
`git clone 'Repository URL'`

****

#### Status

Show the working tree status. <br>
https://git-scm.com/docs/git-status <br>
`git status`

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

#### Remove Files

Remove files from the working tree and from the index. <br>
https://git-scm.com/docs/git-rm <br>
`git rm 'file_name'`

***

#### Commit

Record changes to the repository. <br>
https://git-scm.com/docs/git-commit <br>
`git commit`

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

#### Branch

List, create, or delete branches. <br>
https://git-scm.com/docs/git-branch <br>
`branch`

Local branches in your repository <br>
`git branch`

Remote branches im repository <br>
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

***

#### Pull
Fetch from and integrate with another repository or a local branch. <br>
https://git-scm.com/docs/git-pull <br>
`git pull`

***

#### Rebase
Reapply commits on top of another base tip. <br>
https://git-scm.com/docs/git-rebase <br>
`git rebase`

***

#### Resources:
>[RU] http://dev-labinfo/2013/08/шпаргалка-по-git-основные-команды-слиян/ <br>
[RU] https://ru.hexlet.io/blog/posts/how-to-use-github-badges <br>
[EN] [RU] https://git-scm.com/book/ru/v2 <br>
[EN] https://learngitbranching.js.org/ <br>
[Autocomplete for Mac's Terminal] https://apple.stackexchange.com/questions/55875/git-auto-complete-for-branches-at-the-command-line <br>
[Delete all commit history] https://stackoverflow.com/questions/13716658/how-to-delete-all-commit-history-in-github