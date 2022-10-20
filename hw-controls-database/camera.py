import cv2

class camera:
    def __init__(self):
        '''
            Initializes the camera
        Args:
            None
        Returns:
            None
        '''
        self.cap = cv2.VideoCapture(0)
    
    def getFrame(self):
        '''
            Gets a frame from the camera
            Args:
                None
            Returns:
                frame: the frame from the camera'''
        ret, frame = self.cap.read()
        return frame

    def close(self):
        '''
            Closes the camera
            Args:
                None
            Returns:
                None
                '''
        self.cap.release()


if __name__ == "__main__":
    cam = camera()
    while True:
        frame = cam.getFrame()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.close()
    cv2.destroyAllWindows()
