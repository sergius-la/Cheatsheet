# Branching

| `git branch` | Local branches |
| --- | --- |
| `-a` | All branches local and remote |
| `--merged` | Merged branches |
| `--no-merged` | Unmerged branches |

## Remote

<img src="https://github.com/sergius-la/icon_links/blob/master/img/stackoverflow.png" width="14" height="14"> [__Create a remote branch__](https://stackoverflow.com/questions/1519006/how-do-you-create-a-remote-git-branch)
```shell
git checkout -b <new_branch_name>
git push --set-upstream origin <new_branch_name>
```

__Delete a remote branch__
```shell
git push origin :branch_to_be_deleted
```

***

## Local

[__Rename branch__](https://www.notion.so/Git-a2117392da1d450bb04c1205e6fbd140#9ce31bcf67b24ef7a86ada1f60a064ed)
```shell
# Other branch
git branch -m <oldname> <newname>

# Current branch
git branch -m <newname>
git branch -M <newname>
```

__Detele branch__
```shell
# Merged branch
git branch -d <branch_name>

# Unmerged branch (force)
git branch -D <branch_name>
```