### Commit

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