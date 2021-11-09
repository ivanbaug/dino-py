from PIL.Image import TRANSPOSE
from PIL.ImageOps import grayscale
import win32api
import pyautogui
import time

# apr_region = (0, 167, 520, 345)
apr_region = (127, 290, 123, 73)

pix_loc = (155, 325)
pix_color = (83, 83, 83)

dinos = [
    "project\\img\\dino01.png",
    "project\\img\\dino02.png",
    "project\\img\\dino03.png",
]
cacti = [
    "project\\img\\cactus01.png",
    "project\\img\\cactus02.png",
    "project\\img\\cactus03.png",
    "project\\img\\cactus04.png",
]

x, yold = pix_loc

ys = [335, 325, 315]


for dino in dinos:
    dino_pos = pyautogui.locateOnScreen(
        dino, region=apr_region, grayscale=True, confidence=0.7
    )
    if dino_pos != None:
        dino_x, dino_y, w, h = dino_pos
        win32api.SetCursorPos((dino_x, dino_y))
    else:
        print("dino not found")
# dino_x = 30


# while True:
#     # dino_x = 30
#     # dino_y = 0
#     # cacti_x = []
#     # cacti_y = []
#     pix = pyautogui.pixelMatchesColor(170, 335, pix_color)
#     if pix:
#         print("jump!")
#         pyautogui.press("up")
#     # else:
#     #     # Bird
#     #     bird = pyautogui.pixelMatchesColor(155, 291, pix_color)
#     #     if bird:
#     #         print("duck!")
#     #         pyautogui.keyDown("down")
#     #         time.sleep(0.5)
#     #         pyautogui.keyUp("down")

#     # for y in ys:
#     #     pix = pyautogui.pixelMatchesColor(x, y, pix_color)
#     #     if pix:
#     #         print("jump!")
#     #         pyautogui.press("up")

#     # Single dino position
#     # for dino in dinos:
#     #     dino_pos = pyautogui.locateOnScreen(
#     #         dino, region=apr_region, grayscale=True, confidence=0.8
#     #     )
#     #     if dino_pos != None:
#     #         dino_x, dino_y, w, h = dino_pos
#     #         print(dino_x)
#     # # dino_x = 30
#     # win32api.SetCursorPos()
#     # for cactus in cacti:
#     #     cactus_pos = pyautogui.locateOnScreen(
#     #         cactus, region=apr_region, grayscale=True, confidence=0.8
#     #     )
#     #     if cactus_pos != None:
#     #         cactus_x, cactus_y, w, h = cactus_pos
#     #         cacti_x.append(cactus_x)
#     # print(f"cacti found:{len(cacti_x)}")
#     # for cx in cacti_x:
#     #     if cx - dino_x < 160:
#     #         print("jump!")
#     #         pyautogui.press("up")
