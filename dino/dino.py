import pyscreenshot
import cv2
import numpy as np
import pyautogui
from time import sleep
# 600 x 150
x, y, w, h = 170, 350, 200, 100

speed_tracker = 0

while True:
	cactus_window = np.array(pyscreenshot.grab(bbox=(x, y, x + w, y + h)))
	cactus_window = cv2.cvtColor(cactus_window, cv2.COLOR_BGR2GRAY)
	
	speed_tracker += 1
	
	if speed_tracker < 400 and speed_tracker % 20 == 0:
		x += 3 if x <= 250 else 1
		w += 2
		print(speed_tracker, x, w)
	
	cv2.imshow("Full window", cactus_window)
	cv2.imshow("Upper eye", cactus_window[40 : 50, :])
	cv2.imshow("Lower eye", cactus_window[-15 : , :])
	k = cv2.waitKey(1)
	if k & 0xFF == ord('q'):
		break
	if not ((cactus_window[-15 : , : ] == 255).all() or (cactus_window[-15 : , :] == 0).all()):
		pyautogui.press('space')
	elif not ((cactus_window[40 : 50, : ] == 255).all() or (cactus_window[40 : 50, :] == 0).all()):
		pyautogui.keyDown('down')
		sleep(0.5)
		pyautogui.keyUp('down')
'''	if not (cactus_window == (np.ones((40, 170)) * 255)).all():
		body.send_keys(Keys.SPACE)'''

cv2.destroyAllWindows()
print("yo!")
