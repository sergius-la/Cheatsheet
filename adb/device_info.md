# Device Info

### `dumpsys` 

`adb shell dumpsys` - is a tool that runs on Android devices to get diagnostic output for all system services running on a device.

### [adb docs: dumpsys](https://developer.android.com/studio/command-line/dumpsys)

List of Services on the device <br> 
`adb shell dumpsys | grep <DUMP OF SERVICE>`

Screen resolution <br> 
`adb shell dumpsys display | grep density`

#### `dumpsys window`

> Package Name & Activity Name from current window. <br>
`adb shell dumpsys window windows | grep -E 'mCurrentFocus'`

#### Bluetooth

Get infromation about Bluetooth <br> 
`adb shell dumpsys bluetooth_manager`

Get information about conected device <br>
`adb shell dumpsys bluetooth_manager | grep -A1 Bonded`

***

### `getprop`

`adb shell getprop`

[Android System Properties and Local Preferences](https://developer.oculus.com/documentation/mobilesdk/1.0.3/concepts/mobile-localprefs/)

Android device: <br>
`adb shell getprop ro.product.manufacturer` <br>
`adb shell getprop ro.product.model` <br> 
`adb shell getprop ro.product.device` <br>
`adb shell getprop ro.build.version.release` <br> 
`adb shell getprop ro.serialno` <br>
`adb shell getprop ro.operator.alpha`

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

## PID

[_PID of the particular process_](https://stackoverflow.com/questions/21319883/adb-find-pid-from-the-adb-shell)

#### pidof

`adb shell pidof <package.name>`

#### ps

`adb shell ps | grep <package.name> | cut -d ' ' -f 5`

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

## Networking

### IP Adress

Device IP address <br>
`adb shell ip addr`