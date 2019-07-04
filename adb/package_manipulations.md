# Application (package) manipulation

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
