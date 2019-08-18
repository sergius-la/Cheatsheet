# Bash Profile

## Alias

`Push all`

```bash
pha() {
    git add .
    git commit -m "$1"
    git push
}
```

`Push Master` from Local Dev (track master)

```bash
push-master() {
    git checkout master
    git merge dev
    git push
    git checkout dev
}
```