# Android Debug Bridge (adb)

[Android Developer](https://developer.android.com/studio/command-line/adb) - Android debug bridge documentation  

***

> Debugging tools: <br>
uiautomatorviewer -- Android Automation Viewer <br>
monitor -- Android Monitor

List of all connected devices <br>
`adb devices`

> Work with a particular device <br>
`adb -s 'device'`

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
`adb shell input keyevent 'event_number'`

Tap X,Y position. <br> 
`adb shell input tap 'X' 'Y'`

Swipe X1 Y1 X2 Y2. <br> 
`adb shell input swipe 'X1' 'Y1' 'X2' 'Y2'`

***

### Device information

List of Services on the device <br> 
``` adb shell dumpsys | grep "DUMP OF SERVICE" ```

List of Process on the device <br> 
``` adb shell top ```

Screen resolution <br> 
``` adb shell dumpsys display | grep density ```

Get Information from Device <br>
`adb shell getprop`

***

#### Bluetooth

Get infromation about Bluetooth <br> 
``` adb shell dumpsys bluetooth_manager ```

Get information about conected device <br>
`adb shell dumpsys bluetooth_manager |  grep -A1 Bonded`

***

#### Getprop

Get info about device <br>
`getprop ro.product.model; getprop ro.product.device; getprop ro.build.version.release`

`adb shell getprop ro.product.model` 

`adb shell getprop ro.product.device` 

`adb shell getprop ro.build.version.release` 

`adb shell getprop ro.serialno` 

`adb shell getprop ro.operator.alpha`

***

#### Logcat

Run the log from a device <br>
``` adb logcat ```

Clear the log on a device <br>
``` adb logcat -c ```

Dump logs from buffer <br>
`adb logcat -d`

> Dump log into file <br>
`adb logcat -d >'file_name'.txt`

Log for package <br>
TODO


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

Launch Application <br>
`adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n 'package_name'/'activity_name'`

Close Application <br>
``` adb shell am force-stop "package_name" ```

Clear Application cache <br>
``` adb shell pm clear "package_name" ```

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

-- Packages list --

-f full path
-e enabled packages
-s system packages
-3 third party packages 
  
pm list packages -- list all packages on your device
pm list packages -f -- list all packages on your device with locations

adb shell pm clear <package> -- This will delete all data associated with a package.



-- Package Name & Activity Name from current window  --
adb shell dumpsys window windows | grep Focus


-- How to find name on the Package --
adb shell
pm list packages | grep "name"


-- How to find version of the Package --
adb shell dumpsys package <packageName> | grep version

Push -- Copy file to Device/Emulator

adb -s __serial number__ push /__directory_name__/__file_name__ /__device_directory__ 
adb -s emulator-5554 push ~/Desktop/123.txt /sdcard


Pull -- Copy File from Device/Emulator

adb -s __serial number__ pull /__device_directory__/__file_name__ /__directory_name__ 
adb -s emulator-5554 pull /sdcard/1234.txt .

***

-- Make a Screenshot --
adb -s "serial number" shell screencap /"device_directory"/"file_name"
adb -s emulator-5554 shell screencap /sdcard/sc2.png
--


-- Screenshot & Copy to Desktop -- 
adb shell  screencap /sdcard/"3.png" | adb  pull /sdcard/"3.png" /Users/sergey/Desktop 
--




-- Make a Screenrecord --
-bit
--


adb -s "serial number" shell screenrecord --time-limit "seconds" /"device_directory"/"file_name.mp4"
adb shell screenrecord --time-limit 15 /sdcard/1.mp4
adb -s emulator-5554 shell screenrecord --time-limit 15 /sdcard/happy.mp4


-- Screenrecord & Copy to Desktop --
adb shell screenrecord --time-limit 60 /sdcard/1.mp4
adb  pull /sdcard/1.mp4 /Users/sergey/Desktop

adb shell screenrecord --time-limit "60" /sdcard/"1.mp4"
adb  pull /sdcard/"1.mp4" /Users/sergey/Desktop
--

***

