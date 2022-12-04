import cv2

training_face_data = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml')

# img = cv2.imread('im1.webp')
webcam = cv2.VideoCapture(0)
while True:
    successfull_fame, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect Faces
    face_coordinates = training_face_data.detectMultiScale(grayscaled_img)
    # print(face_coordinates)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("FACE DETECTOR BY ABHINAV BHARDWAJ", frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break
webcam.release()
