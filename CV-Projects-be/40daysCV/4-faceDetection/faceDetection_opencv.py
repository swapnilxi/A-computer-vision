import cv2

# Load an image
image = cv2.imread('/Users/abundent/Documents/coding/Python/A-computer-vision/40daysCV/frontend/src/app/courses/computer-vision/projects/ImagesData/shiva.jpeg')

# Display the image
cv2.imshow('Original Image', image)
if cv2.waitKey(0) & 0xFF == ord('q'):  # Press 'q' to exit
    cv2.destroyAllWindows()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the Haar cascade
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces
faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Detected Faces', image)
if cv2.waitKey(0) & 0xFF == ord('q'):  # Press 'q' to exit
    cv2.destroyAllWindows()