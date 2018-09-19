<!-- ```sh
> description
command
``` -->

> Resources:
 [RU] http://dev-labinfo/2013/08/шпаргалка-по-git-основные-команды-слиян/

```sh
> Create a new Git repository
git init
```

```sh
> Copy of the target repository
git clone 'Repository URL'
```

***

### Add / Remove Files

```sh
> Add Files
git add "file"
```

```sh
> Remove Files
git rm "file"
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

***

> Save changes on local computer after pull
git stash
git pull
git stash pop


***

> git add -A stages all changes
git add . stages new files and modifications, without deletions
git add -u stages modifications and deletions, without new files

***
