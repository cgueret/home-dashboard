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

# Notes
To run the server:
```
env FLASK_APP=main.py flask run
```
or
```
python main.py
```
