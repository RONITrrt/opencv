import cv2

# Correct path to the Haarcascade file
faceCascade = cv2.CascadeClassifier("resources/haarcascades/haarcascade_frontalface_default.xml")

# Load the image
img = cv2.imread("resources/img.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


# Display the output
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
