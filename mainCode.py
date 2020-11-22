#!/usr/bin/env python
# coding: utf-8

# In[53]:


import cv2
import numpy as np
i=0
key = cv2.waitKey(1)
webcam = cv2.VideoCapture(0)

while True:

    check, frame = webcam.read()
#   for i in range(0, 5):
    frame = cv2.flip(frame,1)
    framecp = frame.copy()
    cv2.rectangle(framecp,(390,80),(640,380),(70,0,70), 3)
    cv2.circle(framecp, (515,230), 3, (70,0,70), 3)
    cv2.imshow("Capturing", framecp)
    subimg = frame[80:380,390:640]
    img_new = cv2.cvtColor(subimg, cv2.COLOR_BGR2GRAY)
    thres,_,_,_ = cv2.mean(img_new[123:127,98:102])
    h,w = img_new.shape
    rng = 40
    for i in range(h):
        for j in range(w):
            if img_new[i,j]>thres+rng:
                img_new[i,j] = 0
            elif img_new[i,j]<thres-rng:
                img_new[i,j] = 0
            else:
                img_new[i,j] = 255
    cv2.imshow("Sub Image",img_new)
    key = cv2.waitKey(1)
         
    if key == ord('s'):
        cv2.imwrite(filename=str(i)+'_saved_img.jpg', img=subimg)
        webcam.release()
        img_new = cv2.imread(str(i)+'_saved_img.jpg', cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Captured Image", img_new)
       # cv2.waitKey(1650)
        #cv2.destroyAllWindows()
        #print("Processing image...")
        #img_new = cv2.imread(str(i)+'_saved_img.jpg', cv2.IMREAD_ANYCOLOR)
        #print("Converting RGB image to grayscale...")
        #gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
        #print("Converted RGB image to grayscale...")
        #print("Converting Gray image to Binary...")
        #retval, dimage = cv2.threshold(img_new, 120, 255, cv2.THRESH_BINARY)
        #cv2.imshow("Testing",dimage)
        thres,_,_,_ = cv2.mean(img_new[123:127,98:102])
        h,w = img_new.shape
        rng = 40
        for i in range(h):
            for j in range(w):
                if img_new[i,j]>thres+rng:
                    img_new[i,j] = 0
                elif img_new[i,j]<thres-rng:
                    img_new[i,j] = 0
                else:
                    img_new[i,j] = 255
            
        cv2.imshow("Thresholded",img_new)
        kernel = np.ones((2,2), np.uint8)
        img_erode = cv2.erode(img_new, kernel, iterations = 3)
        img_dilate = cv2.dilate(img_erode, kernel, iterations = 3)
        cv2.imshow("dilated",img_dilate)
        #print("Converted Gray image to Binary...")
        #print("Resizing image to 28x28 scale...")
        img_ = cv2.resize(img_new, (224, 224))
        #print("Resized...")
        img_resized = cv2.imwrite(filename=str(i)+'_saved_img-final.jpg', img=img_)
        cv2.imwrite(filename=str(i)+'_saved_img-dialated.jpg', img=img_dilate)
        #print("Image saved!")
        i = i+1
        webcam = cv2.VideoCapture(0)

    elif key == ord('q'):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break


# In[ ]:





# In[ ]:




