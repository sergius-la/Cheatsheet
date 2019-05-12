# XCUITest


Xcode -> Open developer tools -> `Accessibility Inspector`

***

```swift
import XCTest

// Test class extend - XCTestCase
class CalculatorUITests: XCTestCase {
        
    override func setUp() {
        super.setUp()
        continueAfterFailure = false
        XCUIApplication().launch()
    }
    
    override func tearDown() {
        super.tearDown()
    }
    
    // Test method starts with - test
    func testHelloWorld() {
        let app = XCUIApplication(bundleIdentifier: <app.name>)
        print("Hello World")
    }
}
```

[_GitHub: Native App Bundle Identifiers_](https://github.com/joeblau/apple-bundle-identifiers)
- Settings: `com.apple.Preferences`
- App Store: `com.apple.AppStore`
- Safari: `com.apple.mobilesafari`

## XCUIElements

- app.buttons
- app.staticTexts
- app.switches
- tables.cells.staticTexts

## XCUIElement methods

- exists -> boolean
- isSelected -> boolean
- tap()

#### Buttons

Get button by label
```swift
let app = XCUIApplication()
app.buttons[<"label">]
```
Find all buttons

```swift
let app = XCUIApplication()
let buttons = app.buttons.allElementsBoundByIndex
```
