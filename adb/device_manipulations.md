# Device manipulation

### `reboot`

Reboot the device. <br>
`adb reboot`

Reboots into bootloade. <br>
`adb reboot bootloader`

***

## Screen

[Set screen / display brightness](https://github.com/Genymobile/scrcpy/issues/101) <br>
`adb shell settings put system screen_brightness (0 to 255)`

***

## Bluetooth

Bluetooth turn off (need permition) <br> 
`adb shell service call bluetooth_manager 8`

Bluetooth turn on (need permition) <br> 
`adb shell service call bluetooth_manager 6`

***

#### Make a Screenshot

> [Screenshot to computer](https://blog.shvetsov.com/2013/02/grab-android-screenshot-to-computer-via.html) <br>
> `adb shell screencap -p | perl -pe 's/\x0D\x0A/\x0A/g' > screen.png`

`adb shell screencap <path_save_device>` <br>
`adb shell screencap /sdcard/sc2.png`

***

### `input`

[adb docs: List of events](https://developer.android.com/reference/android/view/KeyEvent) 

Input keyevent. <br>
`adb shell input keyevent <event_number>` <br>
`adb shell "input keyevent --longpress 26 && input keyevent --longpress 24"`

Tap X, Y position. <br> 
`adb shell input tap <X> <Y>`

Swipe by coordinates X1 Y1 X2 Y2. <br> 
`adb shell input swipe <X1> <Y1> <X2> <Y2>`

[_Send text_](https://stackoverflow.com/questions/7789826/adb-shell-input-events) <br>
`%s` - Space <br>
`adb shell input text <"Hello%sWorld">`

<!-- press (Default: trackball) -->
<!-- roll <dx> <dy> (Default: trackball) -->