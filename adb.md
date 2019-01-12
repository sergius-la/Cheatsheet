# Android Debug Bridge (adb)

[Android Developer](https://developer.android.com/studio/command-line/adb) - Android debug bridge documentation <br>
[AdbCommands](https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8) - Adb useful commands list 

> Debugging tools: <br>
uiautomatorviewer -- Android Automation Viewer <br>
monitor -- Android Monitor

***

List of all connected devices <br>
`adb devices`

> Work with a particular device <br>
`adb -s <device>`

| Command | Key | Description |
| --- |  --- | --- |
| adb | -d | Work with a real device |
| adb | -e | Work with an emulator |

Close Emulator <br>
``` adb emu kill  ```
***

### Device manipulation

Reboot the device. <br>
`adb reboot`

Reboots into bootloade. <br>
`adb reboot bootloader`

Bluetooth to disable (need permition) <br> 
`adb shell service call bluetooth_manager 8`

***

#### Key Event
[List of events](https://developer.android.com/reference/android/view/KeyEvent) - Android developer documentation 

Input keyevent. <br>
`adb shell input keyevent <event_number>` <br>
`adb shell "input keyevent --longpress 26 && input keyevent --longpress 24"`

Tap X,Y position. <br> 
`adb shell input tap <X> <Y>`

Swipe by coordinates X1 Y1 X2 Y2. <br> 
`adb shell input swipe <X1> <Y1> <X2> <Y2>`

***

### Device information

#### Dumpsys
`dumpsys` is a tool that runs on Android devices to get diagnostic output for all system services running on a device. <br>
https://developer.android.com/studio/command-line/dumpsys

List of Services on the device <br> 
``` adb shell dumpsys | grep "DUMP OF SERVICE" ```

Screen resolution <br> 
``` adb shell dumpsys display | grep density ```

***

#### Memory info
Snapshot of RAM memory usage <br>
`adb shell dumpsys meminfo`

Monitor your system's virtual memory usage<br>
`adb shell vmstat`

Snapshot of how your app's memory is divided between different types of RAM <br>
`adb shell dumpsys meminfo <com.package>`

List of Process on the device <br> 
``` adb shell top ```

***

#### Bluetooth

Get infromation about Bluetooth <br> 
``` adb shell dumpsys bluetooth_manager ```

Get information about conected device <br>
`adb shell dumpsys bluetooth_manager |  grep -A1 Bonded`

***

#### Getprop
Android System Properties and Local Preferences
https://developer.oculus.com/documentation/mobilesdk/1.0.3/concepts/mobile-localprefs/ <br>
`adb shell getprop`

Get Android device manufacturer. <br>
`adb shell getprop ro.product.manufacturer`

`adb shell getprop ro.product.model` 

`adb shell getprop ro.product.device` 

`adb shell getprop ro.build.version.release` 

`adb shell getprop ro.serialno` 

`adb shell getprop ro.operator.alpha`

***

#### Logcat
Logcat is a command-line tool that dumps a log of system messages, including stack traces when the device throws an error and messages. <br>
https://developer.android.com/studio/command-line/logcat

Run the log from a device <br>
``` adb logcat ```

Clear the log on a device <br>
``` adb logcat -c ```

Dump logs from buffer <br>
`adb logcat -d`

> Dump log into file <br>
`adb logcat -d >'file_name'.txt`

[//]: #TODO: (Log for package)


| Command | Description |
| ------ | ------ |
| adb logcat *:E | Error logs only |
| abd logcat *:F | Fatal logs only |
| adb logcat *:I | Information logs only |
| adb logcat *:V | Verbose logs only |
| adb logcat *:D | Debugging logs only |
| adb logcat *:W | Warning logs only |

***

### Application manipulation

#### am (activity manager)
[activity manager](https://gist.github.com/tsohr/5711945) - Android activity manager "am" command help 

Start Application <br>
`adb shell am start <package.name>/<activity_name>`

Start Application without activity name <br>
`PKG=<package.name>` <br>
`adb shell am start $PKG/$(adb shell cmd package resolve-activity -c android.intent.category.LAUNCHER $PKG | sed -n '/name=/s/^.*name=//p')`

Start Service <br>
`adb shell am startservice <service.name>`

Close Application <br>
``` adb shell am force-stop <service.name> ```

Open Market for Particulaar Application <br>
`adb shell am start -a android.intent.action.VIEW -d 'market://details?id=<package.name>'`

#### pm (package manager)
Clear Application cache <br>
``` adb shell pm clear <service.name> ```

***

#### Install

Install Application <br>
``` adb install "path"/"file_name.apk" ```

Replace / Reinstall Application <br>
``` adb install -r "path"/"file_name.apk" ```

Install Application in a sdcard <br>
``` adb install -s "path"/"file_name.apk" ```

Downgrade Application <br>
``` adb install -d "path"/"file_name.apk" ```

Install on a remote device <br>
``` adb -s "IP":"Port" install "path"/"file_name.apk" ```

***

#### Uninstall

Delete Application <br>
``` adb uninstall "package_name.android" ```

Delete Application, but keep the data after package removal <br>
``` adb uninstall -k "package_name.android" ```

-k keeps the data in the cache after package removal

***

### Monkey Test

Device Monkey Test <br>
``` adb shell monkey "number_of_action" ```

Application Monkey Test <br>
``` adb shell monkey -p "package_name.android" "number_of_action" ```

***

### Networking

netstat -- Show active interten conection

Device IP address 
``` adb shell ip addr ```

Open the Port (Common use: 5555 or 5554) <br>
``` adb tcpip "port_number" ```

Connecting device remote (The port must be open) <br> 
``` adb connect "IP":"port_number" ```

***

#### Shell

adb shell

***

### Packages list

List all packages on your device. <br>
`pm list packages`

All packages on your device with locations. <br>
`pm list packages -f`

-f full path
-e enabled packages
-s system packages
-3 third party packages 

This will delete all data associated with a package.<br>
`adb shell pm clear <package>`

***

### Package / Application Information

#### Dumpsys

Package Name & Activity Name from current window. <br>
`adb shell dumpsys window windows | grep -E 'mCurrentFocus'`

Package version. <br>
`adb shell dumpsys package <com.package.name> | grep version`

#### pm (Package Manager)

How to find name packages. <br>
`adb shell pm list packages | grep <name>`

***


#### Push

`adb push <path>/<filename> /<path_destination>` <br> 
`adb push ~/Desktop/123.txt /sdcard`

***

#### Pull 

`adb -s __serial number__ pull /__device_directory__/__file_name__ /__directory_name__` <br> 
`adb -s emulator-5554 pull /sdcard/1234.txt .`

***

#### Make a Screenshot

`adb -s "serial number" shell screencap /"device_directory"/"file_name"` <br>
`adb -s emulator-5554 shell screencap /sdcard/sc2.png`


***

#### Screenshot & Copy to Desktop
`adb shell  screencap /sdcard/"3.png" | adb  pull /sdcard/"3.png" /Users/sergey/Desktop`

`adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png` <br>
https://blog.shvetsov.com/2013/02/grab-android-screenshot-to-computer-via.html <br>
***


#### Make a Screenrecord
-bit

***


`adb -s "serial number" shell screenrecord --time-limit "seconds" /"device_directory"/"file_name.mp4"` <br>
`adb shell screenrecord --time-limit 15 /sdcard/1.mp4` <br>
`adb -s emulator-5554 shell screenrecord --time-limit 15 /sdcard/happy.mp4`

***

#### Screenrecord & Copy to Desktop
`adb shell screenrecord --time-limit 60 /sdcard/1.mp4` <br>
`adb  pull /sdcard/1.mp4 /Users/sergey/Desktop`

`adb shell screenrecord --time-limit "60" /sdcard/"1.mp4"` <br>
`adb  pull /sdcard/"1.mp4" /Users/sergey/Desktop`

***

> For a list of all the available shell programs <br> 
adb shell ls /system/bin

***
