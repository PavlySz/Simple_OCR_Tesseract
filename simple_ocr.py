'''Simple OCR with Tesseract'''

# Import lbraries
import cv2
import pytesseract


# Read image
img = cv2.imread('image1.jpg')

# Display image
cv2.imshow('Image', img)    # Show the image
cv2.waitKey(0)              # Wait for a user input
cv2.destroyAllWindows()     # Close the window


# Extract text
text = pytesseract.image_to_str(img, oem=3, psm=6)
print(f'I found the following text in the image: {text}')


print('DONE! ^ ^')
print('...for now..')
