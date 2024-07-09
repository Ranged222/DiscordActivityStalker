
# Walthy dick n ballz inc.
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Headless function stuff idk e=xactly
def initialize_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    browser = webdriver.Chrome(options=chrome_options)
    return browser

# Discord login (NO TOKEN IK)
def login_to_discord(browser, email, password):
    browser.get("https://discord.com/login")
    time.sleep(5)  # Let the page load

    try:
        # email
        email_input = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
        email_input.send_keys(email)

        # password
        password_input = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        password_input.send_keys(password)

        # submit
        password_input.submit()

        # Wait 20 sec for login thing to intialize
        WebDriverWait(browser, 20).until(EC.url_contains("discord.com/channels"))

        print("Login successful!")
        return True

    except Exception as e:
        print(f"Login failed. Error: {str(e)}")
        return False

# Get the state
def fetch_user_status(browser):
    try:
        online_status_elem = browser.find_element(By.CSS_SELECTOR, '.avatar_bc9cc2')
        aria_label = online_status_elem.get_attribute('aria-label')
        return aria_label
    except Exception as e:
        print(f"An error occurred while fetching status: {str(e)}")
        return None

# niggers it in log
def write_log_message(log_message, file_path):
    with open(file_path, "a") as log_file:
        log_file.write(log_message + '\n')

# Checks friend state
def track_friend_activity(browser, friend_id):
    last_status = None
    last_status_change = None
    username = None
    log_file_path = "log.txt"
    
    # Skips 5 lines in the ;og.txt (always be sure it wont glitch out :cry:)
    if os.path.exists(log_file_path):
        with open(log_file_path, "a") as log_file:
            log_file.write('\n' * 5)

    browser.get(f"https://discord.com/users/{friend_id}")
    WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.avatar_bc9cc2')))

    next_refresh_time = datetime.now() + timedelta(hours=1)
    next_log_update_time = datetime.now() + timedelta(seconds=10)
    last_time_check = datetime.now()

    while True:
        try:
            if datetime.now() >= next_refresh_time:
                print("\nRefreshing the page...")
                browser.get(f"https://discord.com/users/{friend_id}")
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.avatar_bc9cc2')))
                next_refresh_time = datetime.now() + timedelta(hours=1)

            aria_label = fetch_user_status(browser)
            if aria_label:
                status_text = aria_label.split(', ')[1]
                if username is None:
                    username = aria_label.split(', ')[0]

                current_time = datetime.now()

                if status_text != last_status:
                    if last_status is not None:
                        time_in_last_status = current_time - last_status_change
                        minutes, seconds = divmod(time_in_last_status.total_seconds(), 60)
                        hours, minutes = divmod(minutes, 60)

                        log_message = f"{last_status_change.strftime('%d-%m-%Y %H:%M:%S')} {username} status: {last_status} for {int(hours)}:{int(minutes)}:{int(seconds)}"
                        print(log_message)
                        write_log_message(log_message, log_file_path)

                    last_status = status_text
                    last_status_change = current_time

                    # Log the initial status
                    log_message = f"{current_time.strftime('%d-%m-%Y %H:%M:%S')} {username} status: {last_status}"
                    print(log_message)
                    write_log_message(log_message, log_file_path)

                # checks every 20 sec
                if (datetime.now() - last_time_check).total_seconds() >= 20:
                    time_in_current_status = datetime.now() - last_status_change
                    last_time_check = datetime.now()

                time_in_current_status = datetime.now() - last_status_change
                minutes, seconds = divmod(time_in_current_status.total_seconds(), 60)
                hours, minutes = divmod(minutes, 60)
                log_message = f"{last_status_change.strftime('%d-%m-%Y %H:%M:%S')} {username} status: {last_status} for {int(hours)}:{int(minutes)}:{int(seconds)}\r"
                print(log_message, end='')

                # 10sec log updarer
                if datetime.now() >= next_log_update_time:
                    write_log_message(log_message, log_file_path)
                    next_log_update_time = datetime.now() + timedelta(seconds=10)

            time.sleep(3)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break

# main print stuff
def main():
    email = input("email: ")
    password = input("password: ")
    friend_id = input("user ID: ")

    browser = initialize_browser()

    if login_to_discord(browser, email, password):
        track_friend_activity(browser, friend_id)

    browser.quit()

if __name__ == "__main__":
    main()
