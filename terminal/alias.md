# Alias

#### macOS 

`.bash_profile`

```shell
alias hw="echo Hello World"
```

List of Shortcuts:

**Absolute path to file**
```shell
function abspath() {
  # $1 : relative filename
  filename=$1
  parentdir=$(dirname "${filename}")

  if [ -d "${filename}" ]; then
      echo "$(cd "${filename}" && pwd)"
  elif [ -d "${parentdir}" ]; then
    echo "$(cd "${parentdir}" && pwd)/$(basename "${filename}")"
  fi
}
```

- Git:
    - Push All
    ```shell
    pha () {
        git add .
        git commit -m "$1"
        git push
    }
    ```