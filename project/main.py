import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SelService
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException

# Setup selenium
chrome_driver_path = "C:\\ChromeDriver\\chromedriver.exe"
# webpg = "chrome://dino" # window resize doesn't work
webpg = "https://elgoog.im/t-rex/"
jump_count = 0
pix_color = (83, 83, 83)

# May make the response a little slower but i like the feedback
def mjump():
    global jump_count
    pyautogui.press("up")
    jump_count += 1
    print(f"jump #{jump_count}")


def run():
    s = SelService(chrome_driver_path)
    browser = webdriver.Chrome(service=s)
    browser.get(webpg)
    browser.set_window_size(1000, 800)
    # weird x offset
    browser.set_window_position(-10, 0)

    # Run the game
    ## First jump
    time.sleep(2)
    mjump()

    while True:
        if pyautogui.pixelMatchesColor(360, 450, pix_color):
            mjump()
        # if second cactus gets too close
        if pyautogui.pixelMatchesColor(290, 450, pix_color):
            mjump()

        try:
            _ = browser.window_handles
        except (InvalidSessionIdException, WebDriverException) as e:
            break

    browser.quit()
    print("The game is over")


if __name__ == "__main__":
    run()
