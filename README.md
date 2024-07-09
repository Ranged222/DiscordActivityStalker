# IMPORTANT NOTE!!!
This DOES not log your LOGIN information, the code is not obsfucated so feel free to CHECK.
I was unable to get cookie login working. So if u have captcha u are cooked.
Please IP authorize beforehand.

# DiscordActivityStalker
Exactly how the title is, automated ACtivity checker.

# prepartion:
$ sudo apt update

$ sudo apt upgrade
(duh ofc)

$ sudo apt install wget

$ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

$ sudo dpkg -i google-chrome-stable_current_amd64.deb

$ sudo apt-get install -f (if errors with the installation occur)

# pip requirements

$ pip install selenium

$ pip install chromedriver-autoinstaller

# usage
$ pyhton3 script.py

# how this works!
It runs a headless instance of google chrome which "stares" at the user their profile, and updates in console once online status changes, and a log.txt file.

