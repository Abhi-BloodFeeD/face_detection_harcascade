# Face Detection App

### USING HAAR CASCADE ALGORITHM

\*Haar cascade is an algorithm that can detect objects in images, irrespective of their scale in image and location.

Following Code creates a cascade classifier based on pre-prepared dataset input

[Download Link for haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)

```Python3
training_face_data = cv2.CascadeClassifier(
'haarcascade_frontalface_default.xml')
```

\*Library Used -

OpenCV

Steps -

1. Already prepared Trained Dataset Model imported from opencv repository on gitlab
2. Use CascadeClassifier Model
3. Convert image to greyscale , dataset is prepared on greyscaled training datasets for ease of processing

```Python3
cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

4. Detect Multiscale implemented on the input test dataset
5. Rectangle drawn over the coordinates gathered from above model
