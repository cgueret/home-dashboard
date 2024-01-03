# Overview
Code to run a dashboard like that one

![alt text](https://github.com/cgueret/home-dashboard/blob/master/dashboard.png?raw=true)


# Installation
Install dependencies on dietpi:
```
sudo apt-get install python python3-flask python3-bs4 python3-requests
```

Configure kiosk mode: https://dietpi.com/docs/software/desktop/#chromium

```
sudo cp home-dashboard.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable home-dashboard
sudo systemctl start home-dashboard
```

Then, follow the tips on https://dietpi.com/forum/t/non-interactive-rpi-kiosk-improvements/14886 to improve the settings.

Modify /var/lib/dietpi/dietpi-software/installed/chromium-autostart.sh with:
```
CHROMIUM_OPTS="--kiosk --no-crash-upload --disable-breakpad --disable-crash-reporter --incognito --disable-translate --no-first-run --fast --fast-start --disable-features=TranslateUI --disk-cache-dir=/dev/null --disk-cache-size=1 --password-store=basic --start-fullscreen --noerrdialogs --disable-infobars --window-size=800,480 --window-position=0,0"

exec "$STARTX" "$FP_CHROMIUM" $CHROMIUM_OPTS "${URL:-https://dietpi.com/}" -- -nocursor
```

# Notes
To run the server:
```
env FLASK_APP=main.py flask run
```
or
```
python main.py
```
