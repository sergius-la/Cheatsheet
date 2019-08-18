# <img src="https://github.com/sergius-la/icon_links/blob/master/img/bash.png" width="28" height="28"> Bash

### [`Bash Profile`](/bash/bash_profile.md)

Hello World

```bash
VAR="Hello World" 
echo $VAR
```

Print Environment variable

```bash
echo $<ENV_VARIABLE>
echo $PATH
echo $HOME
```


Run script:
```shell
$ /executable_script.sh # chmod +x executable_script.sh
$ sh script.sh 
```

## Variables

Store command output into varialbe

```bash
PY=echo which python
echo $PY
```

Simple flag check
```bash
check() {
    if [ "$1" != "-one" ]; then
        echo "Not One"
    else 
        echo "One"
    fi
}
```