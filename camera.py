import cv2

class VideoCamera:
    def __init__(self, detector):
        self.video = cv2.VideoCapture(0)
        self.detector = detector

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, frame = self.video.read()
        if not success:
            return None

        # Apply object detection
        result_frame = self.detector.detect_objects(frame)

        # Encode to JPEG
        ret, jpeg = cv2.imencode('.jpg', result_frame)
        return jpeg.tobytes()
