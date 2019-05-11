# Alias

#### macOS 

`.bash_profile`

```shell
alias hw="echo Hello World"
```

List of Shortcuts:
- Git:
    - Push All
    ```shell
    pha () {
        git add .
        git commit -m "$1"
        git push
    }
    ``` 