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