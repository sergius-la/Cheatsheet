# Android Debug Bridge (adb)

- [Android debug bridge docs](https://developer.android.com/studio/command-line/adb)
- [Adb useful commands list](https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8) 


Android SDK debugging tools:
- uiautomatorviewer -- Android Automation Viewer
- monitor -- Android Monitor

Android SDK path:
- Windows: `C:\Users\<username>\AppData\Local\Android\sdk`
- Mac: `/Users/<username>/Library/Android/sdk`

PyPackage - [ADB Commands](https://github.com/sergius-la/adb)

***

## Commands

- __ADB:__
  - `devices`
- __[Device info:](/adb/device_info.md)__
  - `dumpsys`
    - Bluetooth
  - `getprop`
  - Memory Usage
  - Process ID
  - `Logcat`
- __[Device manipulations:](/adb/device_manipulations.md)__
  - `reboot`
  - `screen / brightness`
  - Bluetooth on/off
- __[User actions:](/adb/user_actions.md)__
  - `input keyevent <event_num>`
  - `input swipe`
  - `input tap`
- __[Package manipulations:](adb/package_manipulations.md)__
  - `am` (activity manager)
  - `pm` (package manager)
  - `install`
  - `uninstall`
<!-- - __Files:__
  - pull(path_from, path_to)
  - TODO: Push File
- __Package info:__
  - get_list_packages()
  - get_packahe_version(package)
- __Layout:__
  - dump_layout()
  - TODO: Save layout
  - TODO: Search Element -->

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

#### dumpsys input
Dumps the state of the system’s input devices, such as keyboards and touchscreens, and the processing of input events<br>

`adb shell dumpsys netstats detail`

***

#### dumpsys netstats

Inspect network diagnostics<br>
`adb shell dumpsys input`

***

#### top
List of Process on the device <br> 
`adb shell top`

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
