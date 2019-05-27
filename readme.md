# Display connected devices for Hitron CGNM-2250 Router (Shaw)

Uses Selenium Webdriver to login to your router and display connected devices. 
Easily modified for other purposes.

Yes, there is likely a much better method than having to open a web browser.

## Requirements

Python

Selenium + Chromedriver
```
pip install selenium
```

```
pip install chromedriver
```

## Running

First update "myUsername" and "myPassword" with your...

```
python devices.py
```

### Working as of software version: 4.5.11.9.1

### P.S. The modem has a limit on the number of times you can login... "30 per session"