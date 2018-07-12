# Cheatsheet - Android Debug Bridge (adb)

[Android Developer](https://developer.android.com/studio/command-line/adb) - Android debug bridge documentation  

Debugging tools
| Command | Tool |
| ------ | ------ |
| uiautomatorviewer | Automation viewer |
| monitor | Android Monitor |

> List of connected devices
```
adb devices 
```

| Command | Description |
| ------ | ------ |
| adb -d | Work with a real device |
| adb -e | Work with an emulator |
| adb -s | Work with a particular device by serial number |

> Close Emulator
```
adb emu kill 
```

### Device manipulation
> Reboot device
```
adb reboot
```

> Key Event
> [List of events](https://github.com/sergius-la/ADB/blob/master/ADB%20-%20KeyEvent)
```sh
adb shell input keyevent "event number"
adb -s emulator5554 shell input keyevent 7
```

### Device information
| Command | Description |
| ------ | ------ |
| adb shell getprop ro.product.model | |
| adb shell getprop ro.product.device | |
| adb shell getprop ro.build.version.release | |
| adb shell getprop ro.serialno | |
| adb shell getprop ro.operator.alpha | |


> List of Services on the device
```
adb shell dumpsys | grep "DUMP OF SERVICE"
```

> List of Process on the device
```
adb shell top
```

> Screen resolution
```
adb shell dumpsys display | grep density
```

> Get infromation about Bluetooth
```
adb shell dumpsys bluetooth_manager
```

### Get Logs from a Device

> Run the log from a device
```
adb logcat
```

> Clear the log on a device
```
adb logcat -c
```

| Command | Description |
| ------ | ------ |
| adb logcat *:E | Error logs only |
| abd logcat *:F | Fatal logs only |
| adb logcat *:I | Information logs only |
| adb logcat *:V | Verbose logs only |
| adb logcat *:D | Debugging logs only |
| adb logcat *:W | Warning logs only |

### Application manipulation
> Launch Application
```sh
adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n "package_name"/"activity_name"
```

> Close Application
```sh
adb shell am force-stop "package_name"
```

> Clear Application cache
```sh
adb shell pm clear "package_name"
```

> Install Application
```sh
adb install "path"/"file_name.apk"
adb install /Users/DisplayRire/Desktop/com.display_ride.mobile.apk
```

> Replace / Reinstall Application
```sh
adb install -r "path"/"file_name.apk"
```

> Install Application in a sdcard
```sh
adb install -s "path"/"file_name.apk"
```

> Downgrade Application
```sh
adb install -d "path"/"file_name.apk"
```

> Install on a remote device
```sh
adb -s "IP":"Port" install "path"/"file_name.apk"
```

> Delete Application
```sh
adb uninstall "package_name.android"
```

> Delete Application, but keep the data after package removal
```sh
adb uninstall -k "package_name.android"
```

### Monkey Test

> Device Monkey Test
```sh
adb shell monkey "number_of_action"
adb -s emulator-5554 shell monkey 5000
```

> Application Monkey Test
```sh
adb -s "serial number" shell monkey -p "package_name.android" "number_of_action"
adb -s emulator-5554 shell monkey -p com.google.android.youtube 5000
```

### Networking

> Device IP address 
```sh
adb shell ip addr
```

> Open the Port
Common use: 5555 or 5554
```sh
adb tcpip "port_number"
```

> Connecting device remote 
The port should be opend. 
```sh
adb connect "IP":"port_number"
```






