# Android Debug Bridge (adb)

[Android Developer](https://developer.android.com/studio/command-line/adb) - Android debug bridge documentation  

***

| Command | Debugging tool |
| ------ | ------ |
| uiautomatorviewer | Automation viewer |
| monitor | Android Monitor |

List of all connected devices <br>
`adb devices`

| Command | Key | Description |
| --- |  --- | --- |
| adb | -d | Work with a real device |
| adb | -e | Work with an emulator |
| adb | -s | Work with a particular device by serial number |

Close Emulator <br>
``` adb emu kill  ```
***

### Device manipulation

Reboot the device. <br>
`adb reboot` <br>

Reboots into bootloade. <br>
`adb reboot bootloader` <br>

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

Get infromation about Bluetooth <br> 
``` adb shell dumpsys bluetooth_manager ```


`adb shell getprop ro.product.model` 

`adb shell getprop ro.product.device` 

`adb shell getprop ro.build.version.release` 

`adb shell getprop ro.serialno` 

`adb shell getprop ro.operator.alpha`

***

### Get Logs from a Device

Run the log from a device
``` adb logcat ```

Clear the log on a device
``` adb logcat -c ```

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
``` adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n "package_name"/"activity_name" ```

Close Application <br>
``` adb shell am force-stop "package_name" ```

Clear Application cache <br>
``` adb shell pm clear "package_name" ```

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

Delete Application <br>
``` adb uninstall "package_name.android" ```

Delete Application, but keep the data after package removal <br>
``` adb uninstall -k "package_name.android" ```

***

### Monkey Test

Device Monkey Test <br>
``` adb shell monkey "number_of_action" ```

Application Monkey Test <br>
``` adb shell monkey -p "package_name.android" "number_of_action" ```

***

### Networking

Device IP address 
``` adb shell ip addr ```

Open the Port (Common use: 5555 or 5554) <br>
``` adb tcpip "port_number" ```

Connecting device remote (The port must be open) <br> 
``` adb connect "IP":"port_number" ```