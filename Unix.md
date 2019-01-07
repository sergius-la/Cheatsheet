<!-- | Key | Description |
| --- | --- |
| `` | | -->

# Unix commands

#### Mac Terminal

| Mac Shortcuts | Terminal | 
|--- | --- | 
| New Window | <kbd>⌘ Command</kbd> + <kbd>N</kbd> |  
| New Tab | <kbd>⌘ Command</kbd> + <kbd>T | 

***

#### General Commands

> The "|" (pipe) operator sends the standard output of one command to another command as standard input. It allows commands to be combined in a sequential order

An interface to the on-line reference manuals <br>
`man <command>`

Print name of current/working directory <br>
`pwd`

Display processes <br>
`top`

Print or set the system date and time <br>
`date`

***

Clear the terminal screen

Unix-like <br>
`clear`

Windows <br>
`cls`

***

Remove files or directories <br>
`rm <file_name>`

> Delete all files by extension <br>
`rm <path>/**/*.<extension>` <br>
`rm src/**/*.class`

***

Create a directory <br>
`mkdir <directory_name`

Make multiple directories <br>
`mkdir -p <path>/{<dir_name>,<dir_name>}` <br>
`mkdir -p com/test/{buildings,humands}`

***

Search for files in a directory hierarchy <br>
`find`

Observe directory <br>
`find <directory_name>`

Find all directories <br>
`find ./<directory_name>`

***

Concatenate files and print on the standard output <br>
`cat <file_name>`

| Key | Description |
| --- | --- |
| `cat -b <file_name>` | Open a file with Numbered lines | 

Reading large file that doesn’t fit to the screen <br>
`cat <file_name> | less`

Redirecting the content from one file to another <br>
`cat <file_name> > <new_file>`

***

Get information about file <br>
`file <file_name>`

***

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

***

Change the working directory <br>
`cd <directory_name>`

| Option | Description |
| --- | --- |
| `cd ~` | Move to Home directory |
| `cd /` | Move to Root directory |
| `cd ..` | Will move you up one directory |
| `cd -` | Switch you to the previous directory |

***




ls -l /bin -- Show all Command



-- General








<!-- -- Find --

-i ignore case sensetive

-name "*" -- Search any pattern
-name "*pattern" -- Search by partially pattern name
-size +50M -- Search by file size

find . -name "file_name" -- Finds all the files named in the current directory
find / -name "file_name" -- Find all the files named anywhere on the system

--


__
mv "name_directory" "new_name_director" -- Rename Directory

rm -d "name_directory" -- Delete an empty Directory

rm -r "name_directory" -- Delete Not Empty Directory

-- Работа с директориями









-- Count in a file
wc -l "file_name" -- Count line in a file  
wc -c "file_name" -- Count characters in a file
wc -w "file_name" -- Count words in a file


sort "file_name" > "new_file_name" -- Create a new file sorted file by the First character

tail -n "file_name" -- Get the last line in the file
tail -10 "file_name" -- Get last 10 lines in the file

head -n "file_name" -- Get the first line in the file
head -20 "file_name" -- Get first 20 lines in the file

head -8 "file_name" | tail -7 -- Show range of lines from 2 to 8


-- cp Copy/mv Move File --
cp "file_name" "child_directory_name"/ -- Copy File from Current Directory to the Child Directory

mv "file_name" "child_directory_name"/ -- Move File from Current Directory to the Child Directory

-- cp Copy/mv Move a file from a directory to Another Directory
mv "home_directory"/"directory_name"/././"file_name.extention" "home_directory"/"directory_name"/././
mv /Users/sergey/Desktop/text.txt /Users/sergey/Desktop/SWIFT/Array
--

-- cp Copy/mv Move a file from a directory to Current directory
mv "home_directory"/"directory_name"/././"file_name.extention" .
mv /Users/sergey/Desktop/text.txt .
--

-- Работа с файлами


 -- Pipe Line
 $ cat .bashrc | grep alias | grep color
 ___

-- Vi Text Editior --

i - insert mode
Esc - Comand Mode

:q - Exit
:w - Save

:wq - Save and Exit
Shift ZZ - Save and Exit
-- Vi


-- Create/Rename/Edit/Delete File --

touch "file_name" -- Create a File

rm "file_name" -- Delete a File

mv "file_name" "new_file_name" - Rename a file


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


-- Command Combinatiom
grep -i -v error catalina.out.txt | wc -l
 1003906 -- -v find all now matches to text

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

__
Посмотреть установленные переменные можно командой env
__


less открывает файл и остаётся в этом режиме. Он позволяет перемещаться по файлу вперёд и назад, производить поиск. Одна из отличительных особенностей пейджеров состоит в том, что они одинаково хорошо и быстро работают с файлами любых размеров. Всё потому, что пейджер не пытается загрузить в память весь файл до его отображения. Он грузит только ту часть, которая помещается на экран и при перемещении подгружает остальное.

less предоставляет несколько десятков команд для перемещения по тексту и его поиску, про большинство из них можно прочитать в соответствующем мануале. Здесь же затронем основные:

q — выход
f — вперёд на страницу
b — назад на страницу
если набрать /, затем начать вводить буквы и нажать Enter, то выполнится поиск введённого текста. Перемещение по найденным совпадениям выполняется командой n (переход к следующему совпадению) и командой N (переход к предыдущему совпадению).




__
history
.bash_history
За то, какое количество команд хранится в истории, отвечает переменная окружения HISTFILESIZE.
__


Взаимодействие с операционной системой всегда ведётся от какого-то конкретного пользователя, созданного в системе. Команда whoami позволяет выяснить, кто же я такой

__

tail -f path/to/file не просто выводит последние строчки файла, но ждёт появления новых.

Посмотреть свой идентификатор можно разными способами. первый — команда id -->

***

#### Resources:

> https://explainshell.com