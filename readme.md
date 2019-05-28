# Display connected devices for Hitron CGNM-2250 Router (Shaw)

Uses Selenium Webdriver to login to your router and display connected devices. 

Easily modified for other purposes.

Runs in the background. Takes approx 10 seconds to get data.

## Requirements + Dependencies

Python

Selenium + Chromedriver
```
pip install selenium 
```
[Download chromedriver here:](http://chromedriver.chromium.org/)

## Running

Update "myUsername" and "myPassword" local variables with your...

Update "chromedriverPath" with the path to your chromedriver.exe

To run from terminal:

```
python devices.py
```

### Working as of software version: 4.5.11.9.1

### P.S. The modem has a limit on the number of times you can login per hour (30)