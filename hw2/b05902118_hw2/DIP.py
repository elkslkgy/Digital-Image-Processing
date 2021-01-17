import cv2
import numpy as np
from matplotlib import pyplot as plt

#read the image
img = cv2.imread("DIP.jpg", 0)

#original histogram
hist,bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

#histogram equalization
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

#new histogram
img2 = cdf[img]
hist2,bins = np.histogram(img2.flatten(), 256, [0, 256])
cdf2 = hist2.cumsum()
cdf_normalized2 = cdf2 * hist2.max()/ cdf2.max()

plt.figure(figsize = (12, 7))

#draw the original histogram
plt.subplot(121)
plt.hist(img.flatten(), 256, [0, 256], color = 'r')
plt.plot(cdf_normalized, color = 'b')
plt.legend(('CDF','histogram'), loc = 'upper left')
plt.xlim([0, 256])
plt.title("before")

#draw the new histogram
plt.subplot(122)
plt.hist(img2.flatten(), 256, [0, 256], color = 'r')
plt.plot(cdf_normalized2, color = 'b')
plt.legend(('CDF','histogram'), loc = 'upper left')
plt.xlim([0, 256])
plt.title("after")
plt.savefig('histogram.png', dpi=400)

#merge old and new pictures
res = np.hstack((img,img2)) #stacking images side-by-side
cv2.imwrite('result.png',res)

#show the histograms
plt.show()