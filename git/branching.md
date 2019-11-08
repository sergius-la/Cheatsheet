## Branching

## Remote

<img src="https://github.com/sergius-la/icon_links/blob/master/img/stackoverflow.png" width="16" height="16"> [__Create a remote branch__](https://stackoverflow.com/questions/1519006/how-do-you-create-a-remote-git-branch)
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

***

#### `branch`

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