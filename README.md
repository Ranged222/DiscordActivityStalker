# IMPORTANT NOTE!!!
This DOES not log your LOGIN information, the code is not obsfucated so feel free to CHECK.
I was unable to get cookie login working. So if u have captcha u are cooked.
Please IP authorize beforehand.

# DiscordActivityStalker
Exactly how the title is, automated ACtivity checker.

![image](https://github.com/Ranged222/DiscordActivityStalker/assets/56038167/c6582683-6c1a-4ac8-981c-ab4b56fe7717)


# preparation:
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
$ git clone https://github.com/Ranged222/DiscordActivityStalker (if not done already)

$ pyhton3 script.py

# how this works!
It runs a headless instance of google chrome which "stares" at the user their profile, and updates in console once online status changes, and logs it in a log.txt file.

