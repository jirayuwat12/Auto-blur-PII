import cv2

class AutoBlur():
    def __init__(self) -> None:
        pass

    def blur_card(self, 
                  photo_image,
                  mode = 0):
        '''
        mode :
            1 : Blur the whole card
            2 : Segment the card
            3 : Segment the card and blur the background
        '''
        # copy image
        photo_image = photo_image.copy()


        return photo_image