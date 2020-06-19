import pyautogui
import cv2
from time import sleep
import numpy as np

print("started")
sleep(2)
count = 0
while True:
	screen = np.array(pyautogui.screenshot())
	count += 1
	
	cv2.imwrite("/home/raghu/Desktop/pyfiles/dino/data/down/" + str(count) + ".png", screen)
	
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
print("yo!")
