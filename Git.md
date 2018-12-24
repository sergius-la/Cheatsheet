<!-- ```sh
> description
command
``` -->

# Git


#### Init

```
Create an empty Git repository or reinitialize an existing one
https://git-scm.com/docs/git-init

git init 
```

***

```
Clone a repository into a new directory
https://git-scm.com/docs/git-clone

git clone "Repository URL"
```

****

#### Status

Show the working tree status <br>
https://git-scm.com/docs/git-status <br>
`git status`

***

##### Adding Files

```
Add file contents to the index
https://git-scm.com/docs/git-add

git add 'file_name'

Stages all changes
git add -A 

Stages new files and modifications, without deletions
git add . 

Stages modifications and deletions, without new files
git add -u 
```

***

##### Remove Files

```
Remove files from the working tree and from the index
https://git-scm.com/docs/git-rm

git rm 'file_name'
```

***

##### Commit


Record changes to the repository <br>
https://git-scm.com/docs/git-commit <br>
`git commit`

Add all modified and deleted, use msg for commit message. <br>
`git commit -am "msg"`

Tell the command to automatically stage files that have been modified and deleted, but new files you have not told Git about are not affected. <br>
`git commit -a`

Use the given "msg" as the commit message. <br>
`git commit -m "msg"`

Convenient way to modify the most recent commit. It can also be used to simply edit the previous commit message without changing its snapshot. <br>
`git commit --amend`

***

### Branches

```sh
> Create a dranch and switch to It
git checkout -b "new branch name"
git checkout -b fix20
```

```sh
> See All branches
git branch

> See All merged branches
got branch --merged

> See unmerged branches
git branch --no-merged

> Last Commit
git branch -v

> Delete Branch
git branch -d "branch name"

> Delete Unmerge Branche
git branch -D "branch name"
```

***

```
Deleting the .git folder may cause problems in your git repository. If you want to delete all your commit history but keep the code in its current state, it is very safe to do it as in the following:


Checkout


git log -1

> git checkout --orphan latest_branch
Add all the files

> git add -A
Commit the changes

> git commit -am "commit message"
Delete the branch

> git branch -D master
Rename the current branch to master

> git branch -m master
Finally, force update your repository

> git push -f origin master
PS: this will not keep your old commit history around
```

```
Save changes on local after pull
git stash
git pull
git stash pop

Какая команда git показывает изменения, сделанные в конкретном коммите?

git show

 git add -i, во время которого git показывает фрагменты измененного кода и спрашивает

git reset path/to/file переводит файл из состояния staged в modified
git checkout path/to/file переводит файл из состояния modified в unmodified, то есть по сути эта команда сбрасывает изменения.
```
Rename branch
If you want to rename a branch while pointed to any branch, do:
git branch -m <oldname> <newname>
If you want to rename the current branch, you can do:
git branch -m <newname>
A way to remember this, is -m is for "move" (or mv), which is how you rename files
 
 
 
// Make from two commmit one
If there are multiple commits, you can use git rebase -i to squash two commits into one.
If there are only two commits you want to merge, and they are the "most recent two", the following commands can be used to combine the two commits into one:
 
git reset --soft "HEAD^"
git commit --amend


#### Resources:
- [RU] http://dev-labinfo/2013/08/шпаргалка-по-git-основные-команды-слиян/
- [RU] https://ru.hexlet.io/blog/posts/how-to-use-github-badges
- [EN] [RU] https://git-scm.com/book/ru/v2
- [EN] https://learngitbranching.js.org/
- [Autocomplete for Mac's Terminal] https://apple.stackexchange.com/questions/55875/git-auto-complete-for-branches-at-the-command-line