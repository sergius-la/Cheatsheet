# User actions

#### `input`

[adb docs: List of events](https://developer.android.com/reference/android/view/KeyEvent) 

Input keyevent. <br>
`adb shell input keyevent <event_number>` <br>
`adb shell "input keyevent --longpress 26 && input keyevent --longpress 24"`

Tap X, Y position. <br> 
`adb shell input tap <X> <Y>`

Swipe by coordinates X1 Y1 X2 Y2. <br> 
`adb shell input swipe <X1> <Y1> <X2> <Y2>`

Send text. <br>
% - Space <br>
`adb shell input text <"Hello%World">`

<!-- press (Default: trackball) -->
<!-- roll <dx> <dy> (Default: trackball) -->
 
