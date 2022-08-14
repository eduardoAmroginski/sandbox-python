import cv2

class FaceDetector():
    def detectFaces(path_to_image):

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        image = cv2.imread(path_to_image)

        converted_to_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(converted_to_gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return image


    def showImage(image):
        cv2.imshow('image', image)
        cv2.waitKey()

if __name__ == '__main__':
    image = FaceDetector.detectFaces('./images-test/image-test-2.jpg')
    FaceDetector.showImage(image)