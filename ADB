https://developer.android.com/studio/command-line/adb.html

uiautomatorviewer - Android Automation Viewer
monitor - Android Monitor


-- Get info about device --
getprop ro.product.model; getprop ro.product.device; getprop ro.build.version.release


adb -s "serial number" shell getprop ro.product.model
adb -s "serial number" shell getprop ro.product.device
adb -s "serial number" shell getprop ro.build.version.release
adb -s "serial number" shell getprop ro.serialno
adb -s "serial number" shell getprop ro.operator.alpha
-- Info





Shell -- Open Shell on the device

adb -s __serial number__ shell
adb shell
--



-- Key Event --
adb -s "serial number" shell input keyevent "number"
adb -s emulator-5554 shell input keyevent 7
--


-- List of Process --
adb -s "serial number" shell top



-- Get all Services --
adb shell dumpsys | grep "DUMP OF SERVICE"



-- Get Information from Device --
adb shell getprop
