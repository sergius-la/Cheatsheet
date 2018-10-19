<!-- ```sh
> description
command
``` -->

# Git

> Resources:
 [RU] http://dev-labinfo/2013/08/шпаргалка-по-git-основные-команды-слиян/
 [RU] https://ru.hexlet.io/blog/posts/how-to-use-github-badges
 [EN] [RU] https://git-scm.com/book/ru/v2
 [EN] https://learngitbranching.js.org/

```sh
> Create a new Git repository
git init
```

```sh
> Copy of the target repository
git clone 'Repository URL'
```

***

##### Add Files

```sh
> Add Files
git add "file"

> Stages all changes
git add -A 

> Stages new files and modifications, without deletions
git add . 

> Stages modifications and deletions, without new files
git add -u 
```

##### Remove Files

```sh
> Remove Files
git rm "file"
```

##### Commit

```bash
> TODO: Add Description
git commit -m "comment"
git commit -- amend
git log -1
```

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
