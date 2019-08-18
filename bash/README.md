# Bash

```bash
VAR="Hello World" 
echo $VAR
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