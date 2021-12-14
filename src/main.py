
import cv2 , numpy as np
from core.effet import Effets

Efs = Effets()

img_src = 'assets/img/tom2.png'
img = cv2.imread(img_src,1)
arr = np.asarray(img)


img = Efs.Make(arr,"anime")

cv2.imshow("Cute Kitens", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
