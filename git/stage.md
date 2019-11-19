# Staging

| `git commit` | Record changes to the repository |
| --- | --- |
| `-m <commit message>` | Add commit message |
| `-a` | Commit modified and deleted (exclude new files) |
| `.` | All files: modified, deleted, new |
| `- u` | Only modified |

## Modify commit

**Squash two commits into one**
```git
git reset --soft "HEAD^"
git commit --amend
```

[**Reset the last commit**](https://www.git-tower.com/learn/git/faq/undo-last-commit)
```shell
git reset --soft HEAD~1
```

#### `cherry-pick`

[Git cherry-pick a file](https://stackoverflow.com/questions/5717026/how-to-git-cherry-pick-only-changes-to-certain-files)

Convenient way to modify the most recent commit. It can also be used to simply edit the previous commit message without changing its snapshot. <br>
`git commit --amend`