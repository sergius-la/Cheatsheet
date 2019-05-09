# Android Debug Bridge (adb)

- [Android debug bridge docs](https://developer.android.com/studio/command-line/adb)
- [Adb useful commands list](https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8) 


Android SDK debugging tools:
- uiautomatorviewer -- Android Automation Viewer
- monitor -- Android Monitor

Android SDK path:
- Windows: `C:\Users\<username>\AppData\Local\Android\sdk`
- Mac: `/Users/<username>/Library/Android/sdk`

***

## Devices

> Work with a particular device <br>
`adb -s <device>`

List of all connected devices <br>
`adb devices`

| Command | Key | Description |
| --- |  --- | --- |
| adb | -d | Work with a real device |
| adb | -e | Work with an emulator |

***

## Device information

#### [adb docs: dumpsys](https://developer.android.com/studio/command-line/dumpsys)

`dumpsys` is a tool that runs on Android devices to get diagnostic output for all system services running on a device.

List of Services on the device <br> 
`adb shell dumpsys | grep <DUMP OF SERVICE>`

Screen resolution <br> 
`adb shell dumpsys display | grep density`

#### getprop

[Android System Properties and Local Preferences](https://developer.oculus.com/documentation/mobilesdk/1.0.3/concepts/mobile-localprefs/)<br>
`adb shell getprop`

Android device: <br>
`adb shell getprop ro.product.manufacturer` <br>
`adb shell getprop ro.product.model` <br> 
`adb shell getprop ro.product.device` <br>
`adb shell getprop ro.build.version.release` <br> 
`adb shell getprop ro.serialno` <br>
`adb shell getprop ro.operator.alpha`

***

## Device manipulation

Reboot the device. <br>
`adb reboot`

Reboots into bootloade. <br>
`adb reboot bootloader`

***

## Bluetooth

Get infromation about Bluetooth <br> 
`adb shell dumpsys bluetooth_manager`

Get information about conected device <br>
`adb shell dumpsys bluetooth_manager | grep -A1 Bonded`

Bluetooth turn off (need permition) <br> 
`adb shell service call bluetooth_manager 8`

## User actions

[adb docs: List of events](https://developer.android.com/reference/android/view/KeyEvent) 

Input keyevent. <br>
`adb shell input keyevent <event_number>` <br>
`adb shell "input keyevent --longpress 26 && input keyevent --longpress 24"`

Tap X, Y position. <br> 
`adb shell input tap <X> <Y>`

Swipe by coordinates X1 Y1 X2 Y2. <br> 
`adb shell input swipe <X1> <Y1> <X2> <Y2>`

***

## Memory Usage

#### dumpsys meminfo
Snapshot of RAM memory usage <br>
`adb shell dumpsys meminfo <package.name>` <br>
`adb shell dumpsys meminfo <PID>`

#### procstats
To see how your app is behaving over time—including how long it runs in the background and how much memory it uses during that time<br>
`adb shell dumpsys procstats --hours 3`

#### vmstat
Monitor your system's virtual memory usage<br>
`adb shell vmstat`

***

#### dumpsys input
Dumps the state of the system’s input devices, such as keyboards and touchscreens, and the processing of input events<br>

`adb shell dumpsys netstats detail`

***

#### dumpsys netstats

Inspect network diagnostics<br>
`adb shell dumpsys input`

***

## Processes

#### pidof

[PID of the particular process](https://stackoverflow.com/questions/21319883/adb-find-pid-from-the-adb-shell) <br>
`adb shell pidof <package.name>`

***

#### top
List of Process on the device <br> 
`adb shell top`

***

## Logcat

[adb docs: logcat](https://developer.android.com/studio/command-line/logcat)

> Dump log into file <br>
`adb logcat -d >'file_name'.txt`

Run the log from a device <br>
`adb logcat`

Clear the log on a device <br>
`adb logcat -c`

Dump logs from buffer <br>
`adb logcat -d`

| Command | Description |
| ------ | ------ |
| adb logcat *:E | Error logs only |
| abd logcat *:F | Fatal logs only |
| adb logcat *:I | Information logs only |
| adb logcat *:V | Verbose logs only |
| adb logcat *:D | Debugging logs only |
| adb logcat *:W | Warning logs only |

***

## Application manipulation

#### [am (activity manager command help)](https://gist.github.com/tsohr/5711945)

Start Application <br>
`adb shell am start <package.name>/<activity_name>`

Start Application without activity name <br>
`PKG=<package.name>` <br>
`adb shell am start $PKG/$(adb shell cmd package resolve-activity -c android.intent.category.LAUNCHER $PKG | sed -n '/name=/s/^.*name=//p')`

Start Service <br>
`adb shell am startservice <service.name>`

Close Application <br>
`adb shell am force-stop <service.name>`

Open Market for Particulaar Application <br>
`adb shell am start -a android.intent.action.VIEW -d 'market://details?id=<package.name>'`

***

#### pm (package manager)

Clear Application cache <br>
`adb shell pm clear <service.name>`

List all packages on your device. <br>
`adb shell pm list packages`

| Flag | Description |
| ------ | ------ |
| `pm list packages -f` | full path |
| `pm list packages -e` | enabled packages |
| `pm list packages -s` | system packages |
| `pm list packages -3` | third party packages |

***

#### Install apk

Install Application <br>
`adb install <local_path>/<file_name.apk>`

| Flag | Description |
| ------ | ------ |
| `install -r` | Replace / Reinstall Application |
| `adb install -s` | Install Application in a sdcard |
| `adb install -d` | Downgrade Application |

***

#### Uninstall

Delete Application <br>
`adb uninstall <package_name.android>`

Delete Application, but keep the data after package removal <br>
`adb uninstall -k <package_name.android>`

***

<!-- Application manipulation -->

## Package / Application Information

> Package Name & Activity Name from current window. <br>
`adb shell dumpsys window windows | grep -E 'mCurrentFocus'`

Package version. <br>
`adb shell dumpsys package <com.package.name> | grep version`

***

<!-- Package / Application Information -->

### Networking

netstat -- Show active interten conection

Device IP address 
`adb shell ip addr`

Open the Port (Common use: 5555 or 5554) <br>
``` adb tcpip "port_number" ```

Connecting device remote (The port must be open) <br> 
``` adb connect "IP":"port_number" ```

***

#### Shell

adb shell

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

#### Monkey Test

Device Monkey Test <br>
`adb shell monkey <number_of_action>`

Application Monkey Test <br>
`adb shell monkey -p <package_name.android> <number_of_action>`

***

#### shell

`adb shell start`

`adb shell stop`

***

Close Emulator <br>
``` adb emu kill  ```
