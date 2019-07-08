# Files

#### push

Copy file to device <br>
`adb push <path_from> <path_to>` <br> 
`adb push ~/Desktop/123.txt /sdcard`

***

#### pull 

Copy file from a device <br>
`adb pull <path_from> <path_to>` <br> 
`adb -s emulator-5554 pull /sdcard/1234.txt ~/Desktop/`