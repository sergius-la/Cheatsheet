# Android Debug Bridge (adb)

- [Android debug bridge docs](https://developer.android.com/studio/command-line/adb)
- [Adb useful commands list](https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8) 


Android SDK debugging tools:
- uiautomatorviewer -- Android Automation Viewer
- monitor -- Android Monitor

ADB path:
```shell
ANDROID_SDK=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_SDK/platform-tools:$ANDROID_SDK/tools/bin
```

PyPackage - [ADB Commands](https://github.com/sergius-la/adb)

***

## Commands

- __ADB:__
  - `devices`
  - `Monkey Test: Device/App`
- __[Device info:](/adb/device_info.md)__
  - `dumpsys`
    - Bluetooth
  - `getprop`
  - Memory Usage
  - Process ID
  - `Logcat`
  - `current activity/package`
  - Networking
    - `ip addr`
  - `wm (window manager)`
- __[Device manipulations:](/adb/device_manipulations.md)__
  - `reboot`
  - `screen / brightness`
  - Bluetooth on/off
  - Screenshot
- __[User actions:](/adb/user_actions.md)__
  - TODO: Move to Device Manipulations
  - `input keyevent <event_num>`
  - `input swipe`
  - `input tap`
- __[Package manipulations:](/adb/package_manipulations.md)__
  - `am` (activity manager)
  - `pm` (package manager)
  - `install`
  - `uninstall`
- __[Package info:](/adb/package_info.md)__
  - `dumpsys package`
- __[Files:](/adb/files.md)__
  - `pull`
  - `push`
  <!-- - get_list_packages() -->
  <!-- - TODO: Push File
<!-- - __Layout:__
  - dump_layout()
  - TODO: Save layout
  - TODO: Search Element --> -->

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

***

<!-- Package / Application Information -->

### Networking

netstat -- Show active interten conection

Open the Port (Common use: 5555 or 5554) <br>
``` adb tcpip "port_number" ```

Connecting device remote (The port must be open) <br> 
``` adb connect "IP":"port_number" ```

***

#### Shell

adb shell

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
