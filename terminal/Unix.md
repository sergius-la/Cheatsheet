<!-- | Key | Description |
| --- | --- |
| `` | | -->

# Unix/Linux commands

#### Mac Terminal

| Mac Shortcuts | Terminal | 
|--- | --- | 
| New Window | <kbd>⌘ Command</kbd> + <kbd>N</kbd> |  
| New Tab | <kbd>⌘ Command</kbd> + <kbd>T | 

[_Stack Overflow: Reload bash_profile_](https://stackoverflow.com/questions/4608187/how-to-reload-bash-profile-from-the-command-line)

```shell
source ~/.bash_profile
```

***

#### &&

Executing multiple command use <br>
`cd ~/Desktop && mkdir newfolder`

***

#### General Commands

https://askubuntu.com/questions/334994/which-one-is-better-using-or-to-execute-multiple-commands-in-one-line <br>
A; B # Run A and then B, regardless of success of A
A && B # Run B if and only if A succeeded
A || B # Run B if and only if A failed
A & # Run A in background.

The "|" (pipe) operator sends the standard output of one command to another command as standard input. It allows commands to be combined in a sequential order

> Command > append >>

***

An interface to the on-line reference manuals <br>
`man <command>`

> Show list of all commands in the shell <br>
`ls -l /bin`

Print name of current/working directory <br>
`pwd`

Display processes <br>
`top`

Print or set the system date and time <br>
`date`

Run a program in a modified environment <br>
`env`

Log of commands <br>
`history`

***

Clear the terminal screen

Unix-like <br>
`clear`

Windows <br>
`cls`

***

#### mkdir
Create a directory <br>
`mkdir <directory_name`

Make multiple directories <br>
`mkdir -p <path>/{<dir_name>,<dir_name>}` <br>
`mkdir -p com/test/{buildings,humands}`

***

#### find
Search for files in a directory hierarchy <br>
`find`

Observe directory <br>
`find <directory_name>`

Find all directories <br>
`find ./<directory_name>`

***

#### cat
Concatenate files and print on the standard output <br>
`cat <file_name>`

| Key | Description |
| --- | --- |
| `cat -b` | Open a file with Numbered lines | 

Reading large file that doesn’t fit to the screen <br>
`cat <file_name> | less`

Redirecting the content from one file to another <br>
`cat <file_name> > <new_file>`

***

#### file
Get information about file <br>
`file <file_name>`

***

#### ls
List directory contents <br>
`ls`

| Key | Description |
| --- | --- |
| `ls -a` | Invisible files |
| `ls -l` | Files in a long format |
| `ls -S` | Sort by size |
| `ls -s, --size ` | Print the allocated size of each file, in blocks |

***

### Networking

IP Info <br>
`ifconfig` 

Send ECHO_REQUEST packets to network hosts <br>
`ping <website/IP>`

#### netstat

***

#### cd
Change the working directory <br>
`cd <directory_name>`

| Option | Description |
| --- | --- |
| `cd ~` | Move to Home directory |
| `cd /` | Move to Root directory |
| `cd ..` | Will move you up one directory |
| `cd -` | Switch you to the previous directory |

***
#### cp
Copy files and directories <br>
`cp <path_from/file_name> <path_to>`

***

#### mv
Move (rename) files <br>
`mv <path_from/file_name> <path_to>`

Rename a file <br>
`mv <file_name> <new_file_name>`

***

#### rm
Delete files or directories <br>
`rm <file_name>`

> Delete all files from a directory <br>
`cd <path> && rm -rf *` <br>

> Delete all files by format <br>
`cd <path> && rm -rf *.<ext>` <br>

> Delete all subfolder in the directory <br>
`rm -R -- */` <br>

| Key | Description |
| --- | --- |
| `rm -d` | Delete an empty Directory |
| `rm -r` | Delete Not Empty Directory |
| `rm -f` | Force which is helpful when you don't want to be asked/prompted |

***

#### Vi text editior

i - insert mode <br>
Esc - Comand Mode <br>

:q - Exit <br>
:w - Save <br>

:wq - Save and Exit <br>
Shift ZZ - Save and Exit

***

#### ws
Print newline, word, and byte counts for each file <br>
`ws <file_name>`

| Key | Description |
| --- | --- |
| `wc -l` | Count line in a file  |
| `wc -c` | Count characters in a file  |
| `wc -w` | Count words in a file  |

***

#### passwd 

Change user password - requited root account <br>
`passwd`

***

#### Shortcut

'#' - Comment

<kbd>⌃ Control</kbd> + <kbd>R - Search in the History
<kbd>⌃ Control</kbd> + <kbd>A - Move to Begining
<kbd>⌃ Control</kbd> + <kbd>E - Mo to the End

***

#### ln

Make a link for a file
ln -s file fileLINK

***

#### shutdown

shutdown -r now - Restart now
shutdown -h +60 - TurnOff in 60 nimutes

***

#### w

w - what happening

***

#### mkdir

mkdir -p - Make a full path

***

#### profile

nano ~/.bash_profile

***

#### `grep`

grep --invert-match

* -e pattern.
* -i: Ignore uppercase vs. lowercase.
* -v: Invert match.
* -c: Output count of matching lines only.
* -l: Output matching files only.
* -n: Precede each matching line with a line number.
* -b: A historical curiosity: precede each matching line with a block number.





<!-- sort "file_name" > "new_file_name" -- Create a new file sorted file by the First character

tail -n "file_name" -- Get the last line in the file
tail -10 "file_name" -- Get last 10 lines in the file

head -n "file_name" -- Get the first line in the file
head -20 "file_name" -- Get first 20 lines in the file

head -8 "file_name" | tail -7 -- Show range of lines from 2 to 8





 -- Pipe Line
 $ cat .bashrc | grep alias | grep color
 ___




-- Create/Rename/Edit/Delete File --

touch "file_name" -- Create a File






-- Regular Expressions --

grep "pattern" "file_name" -- Search pattern in the file
grep "pattern1\|pattern2"


-- Get RexEx search and +1 string down -- 
grep -1A __pattern__ __file_name__

-- Get RexEx search and +1 string up --
grep -1B __pattern__ __file_name__

 -i ignore case sensetive
 -v returns lines that do not match the pattern
 -c return the count(number of lines)
 -w return lines where pattern is separate word
 -n preceds each line with the line number
 -r search in any direction
 
--color Return coloring

grep -i "pattern" "file_name" -- Search pattern ignore case sensetive

grep -v "pattern" "file_name" -- Search pattern lines that do not match the pattern



-- RegExp 

-- Unix Permission --

--- --- ---

(d) - directory
(-) - file
(l) - link

First --- Owner (User)
Second --- Group
Find --- Other (word)

Read - r
Writhe/Edit - w
Execute - x

7 - Read/Edit/Execute
5 - Read/Execute

-- Edit Permission --

-- chmod - Change permission
chmod ugo=rwx "file_name" -- Allow all type of ysers Read/Edit/Execute
cmhod 777 "file_name" -- Allow all type of ysers Read/Edit/Execute

cmhod 755 "file_name" -- Allow Owner - Read/Edit/Execute; Group/Other (Read/Execute) 

-- Remove Permission -"type_permission"
chmod go-w "file_name" -- Remove permission Edit for Group and Other

-- Add Permission +"type_permission"
chmod go+w "file_name" -- Add permission Edir for Group and Other

-- Combile different permission
chmod g+wx, o+x "file_name" -- Add permission Edit and Exicute for Group, and Execute for Other


-- chown - Change owner of the file
chown "new_owner" "file_name" -- Change owner of the file

chown :"new_group" "file_name" -- To change groups

-- Permission



How to set a variable to the output of a command in Bash?
OUTPUT="$(ls -1)"
echo "${OUTPUT}"




less открывает файл и остаётся в этом режиме. Он позволяет перемещаться по файлу вперёд и назад, производить поиск. Одна из отличительных особенностей пейджеров состоит в том, что они одинаково хорошо и быстро работают с файлами любых размеров. Всё потому, что пейджер не пытается загрузить в память весь файл до его отображения. Он грузит только ту часть, которая помещается на экран и при перемещении подгружает остальное.

less предоставляет несколько десятков команд для перемещения по тексту и его поиску, про большинство из них можно прочитать в соответствующем мануале. Здесь же затронем основные:

q — выход
f — вперёд на страницу
b — назад на страницу
если набрать /, затем начать вводить буквы и нажать Enter, то выполнится поиск введённого текста. Перемещение по найденным совпадениям выполняется командой n (переход к следующему совпадению) и командой N (переход к предыдущему совпадению).






Взаимодействие с операционной системой всегда ведётся от какого-то конкретного пользователя, созданного в системе. Команда whoami позволяет выяснить, кто же я такой

__

tail -f path/to/file не просто выводит последние строчки файла, но ждёт появления новых.

 -->

***

#### Resources:

> https://explainshell.com