import cv2
  
# Save image in set directory
# Read RGB image
img = cv2.imread('cat.4001.jpg') 
  
# Output img with window name as 'image'
cv2.imshow('image', img) 
  
# Maintain output window utill
# user presses a key
cv2.waitKey(600)        
  
# Destroying present windows on screen
cv2.destroyAllWindows()
