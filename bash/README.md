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

```bash
PY=echo which python
echo $PY
```

## Collections

<img src="https://github.com/sergius-la/icon_links/blob/master/img/stackoverflow.png" width="14" height="14"> [**Stack OverFlow** Hash tables](https://stackoverflow.com/questions/1494178/how-to-define-hash-tables-in-bash)
```bash
declare -A animals=( ["moo"]="cow" ["woof"]="dog")
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

## Functions

```bash
# Function declaration
function main() {
    echo "Hello World"
}
# Call
main
```

## Script Arguments

```bash
# Check all arguments
main $@
```

Script 
```bash
#!/bin/bash

function main() {
    check_args $@
}

function check_args() {
    # echo "Input args:" "<"$@">"
    
    while getopts ":ht" opt; do
        case ${opt} in  
            t ) echo "'T' option is called";;
            h ) help;;
        esac
    done
}

function help() {
    echo "Usage: cmd [-h] [-t]"
}

main $@
```