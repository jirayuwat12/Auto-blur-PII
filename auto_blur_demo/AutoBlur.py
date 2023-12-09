import cv2

class AutoBlur():
    def __init__(self) -> None:
        self.__yolo_model = None

    def blur_card(self,
                  photo_image):
        '''
        Blur the card in the photo_image
        '''
        pass

    def blur(self, 
             photo_image,
             bounding_box):
        '''
        Blur the specified bounding box in the photo_image
        '''
        pass 
    
    def predict(self, 
                photo_image):
        '''
        Detect PII card and return the bounding box
        '''
        pass
