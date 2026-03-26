#! c:\python35
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt # alias新增一個別名，也可以寫 from os import

path=os.getcwd() # get current working directory目前工作的目錄
print('Current working directory=%s' % path)
path="C:\\Users\\fgu\\Desktop\\tmpp"   #需要有兩個反斜線，第一個意思:esc，第二個意思:反斜線  
os.chdir(path)   # change working directory

lena=cv2.imread('ave mujica.jpg',) # ,後面放0是灰階影像模式(Grayscale image)，Width x Height -->資料型態(np.uint8)用來表示介於值0~255的整數，0是黑色，255是白色，其他值是灰色
lena_gray=cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY) # cv2.cvtColor()函數用於轉換圖像的顏色空間，第一個參數是輸入圖像，第二個參數是轉換的代碼，cv2.COLOR_BGR2GRAY表示將BGR(=RGB)圖像轉換為灰階圖像
print(lena.shape); print(lena.ndim); print(lena.dtype) # 一般是寫Width x Height，opencv以列為優先的方式做撰寫所以要做Height x Width，lena.shape會回傳圖像的尺寸，lena.ndim會回傳圖像的維度，lena.dtype會回傳圖像的資料型態
plt.subplot(1,2,1)
lena_rgb=cv2.cvtColor(lena, cv2.COLOR_BGR2RGB)
plt.imshow(lena_rgb)
plt.title('Lena_RGB')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(lena_gray,plt.cm.gray)
plt.title('Lena_Gray')
plt.axis('off')
plt.show()
#cv2.imshow('lena',lena)
#cv2.waitKey()
#cv2.destroyAllWindows()
#--------show lena gray image----
print(lena_gray.shape); print(lena_gray.ndim); print(lena_gray.dtype)
cv2.imshow('lena_gray',lena_gray)
#cv2.waitKey()
#cv2.destroyAllWindows()
#--------write images into files-----
cv2.imwrite('lena_bgr.jpg',lena)
cv2.imwrite('lena_rgb.jpg',lena_rgb) # lena_rgb is not working for cv2.imwrite()
cv2.imwrite('lena_gray.jpg', lena_gray)