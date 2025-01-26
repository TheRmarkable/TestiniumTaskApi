# Login Test

## Scenario: Launch browser, login, verify the Open Money Transfer Button Visible, launch app and verify the page
tags: Login
* Login with ID , password , and browsers "chrome"
* Wait "5000" ms
* The text of the "openButton" element assert "OPEN MONEY TRANSFER"
* Click on "openButton"
* The text of the "verifyApp" element assert "My account"