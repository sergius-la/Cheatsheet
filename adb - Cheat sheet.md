# Cheatsheet - Android Debug Bridge (adb)

[Android Developer](https://developer.android.com/studio/command-line/adb) - Android debug bridge documentation  

| Command | Tool |
| ------ | ------ |
| uiautomatorviewer | Automation viewer |
| monitor | Android Monitor |

```
adb devices 
```
> List of connected devices

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
```sh
adb shell input keyevent "event number"
adb -s emulator5554 shell input keyevent 7
```
[List of events](https://github.com/sergius-la/ADB/blob/master/ADB%20-%20KeyEvent)

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
