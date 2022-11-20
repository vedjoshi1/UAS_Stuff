import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# reading image
img = cv2.imread('IMG_222.jpg')
  
# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
#denoising imgae
img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
  
# using a findContours() function
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
i = 0

# list for storing names of shapes
for contour in contours:
    if(cv2.contourArea(contour) > 50000):
        pass
    else:
         # here we are ignoring first counter because 
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue
       
        if(cv2.contourArea(contour) > 1000):
          
             N = cv2.moments(contour)
             if N['m00'] != 0.0:
                x1 = int(N['m10']/N['m00'])
                y1 = int(N['m01']/N['m00'])
               # print("X " + str(x1) + " Y " + str(y1))
                #cv2.circle(img, (x1,y1), 10, (255,0,0), -1)
                mask = np.zeros(img.shape, np.uint8)
                cv2.drawContours(mask, contour, -1, 255, -1)
          #      mean = cv2.mean(img, mask=mask)
           #     print(mean)
                


        
    
        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(
         contour, 0.01 * cv2.arcLength(contour, True), True)
        
        # using drawContours() function
        #check if there are less than 10 corners in the contour, to remove outrageous ones
        if len(approx) <= 15: 
            #make sure this contour has a reasonable area size //scale this based on
            if(cv2.contourArea(contour) > 1000):
                #
                final = np.zeros(img.shape,np.uint8)
             #   mask = np.zeros(gray.shape,np.uint8)
                
                print(final.ravel());

            
                    #draw contour
                cv2.drawContours(img, [contour], 0, (0, 255, 0), 5)
        
        # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
    
        # putting shape name at center of each shape
      #  if len(approx) == 3:
       #     cv2.putText(img, 'Triangle', (x, y),
        #                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
       # elif len(approx) == 4:
        #    cv2.putText(img, 'Quadrilateral', (x, y),
         #               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        #elif len(approx) == 5:
         #   cv2.putText(img, 'Pentagon', (x, y),
          #              cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        #elif len(approx) == 6:
         #   cv2.putText(img, 'Hexagon', (x, y),
          #              cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
        
            

    
  
# displaying the image after drawing contours
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()