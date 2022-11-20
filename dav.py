from ast import Lambda
import numpy as np
import cv2
#from PIL import Image
from time import sleep

#reading image of the chessboard and creating window. Also making a greyscaled version of the chessboard so as to 
#detect corners
img = cv2.imread('IMG_010.jpg')
img = cv2.resize(img, (0,0), fx = 1, fy = 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#This actually finds the corners and puts it into an array
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 15)
corners = np.int0(corners)


for corner in corners:
    x, y = corner.ravel() #this flattens the array out, removing extraneous aspects of it
  #  print(corner)
    cv2.circle(img, (x,y), 5, (0,255,0), -1) #draws circles on the coloured chessboard of images


#this is the line mapping code, not needed for the DAV project, but just to make it look cool
for i in range(len(corners)):
  for j in range(i+1, len(corners)):
    corner1 = tuple(corners[i][0])
    corner2 = tuple(corners[j][0])    
    color = tuple(map(lambda x: int(x), np.random.randint(0,255,size=3)))
   # cv2.line(img, corner1, corner2,color ,1)
   
  

cv2.imshow('Frame',img)
cv2.waitKey(0) #waits for key press
cv2.destroyAllWindows() #after key press, kills programme