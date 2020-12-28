from matplotlib import pyplot as plt
import matplotlib as mpl
import cv2
import numpy as np
img = cv2.imread('D:/non dehaze/exper/2-2.png', 0)
img_gray = img
img1 = cv2.imread('D:/non dehaze/exper/3-2.png', 0)
img_gray1 = img1
img2 = cv2.imread('D:/non dehaze/exper/4-2.png', 0)
img_gray2 = img2
img3 = cv2.imread('D:/non dehaze/exper/7-2.png', 0)
img_gray3 = img3
img4 = cv2.imread('D:/non dehaze/exper/19-2.png', 0)
img_gray4 = img4
img5 = cv2.imread('D:/non dehaze/exper/47-2.png', 0)
img_gray5 = img5


fig = plt.figure()

ax = fig.add_subplot(331)
hist = cv2.calcHist([img], [0], None, [256],[0,256])
hist1 = cv2.calcHist([img1], [0], None, [256],[0,256])
hist2 = cv2.calcHist([img2], [0], None, [256],[0,256])
hist3 = cv2.calcHist([img3], [0], None, [256],[0,256])
hist4 = cv2.calcHist([img4], [0], None, [256],[0,256])
hist5 = cv2.calcHist([img5], [0], None, [256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist, label='I1P1')
plt.plot(hist1, label='I2P1')
plt.plot(hist2, label='I3P1')
plt.plot(hist3, label='I4P1')
plt.plot(hist4, label='I5P1')
plt.plot(hist5, label='I6P1')

plt.xlim([0, 256])
plt.show()
