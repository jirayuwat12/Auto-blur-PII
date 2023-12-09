import cv2
import torch
import numpy as np
class AutoBlur():
    def __init__(self) -> None:
        self.__yolo_model = torch.hub.load('ultralytics/yolov5', 'custom', path='./weight/best.pt')

    def blur_card(self,
                  photo_image):
        '''
        Blur the card in the photo_image
        '''
        bounding_box = self.predict(photo_image)
        last_image = self.blur(photo_image,bounding_box)
        return last_image

    def blur(self, 
             photo_image,
             bounding_box):
        '''
        Blur the specified bounding box in the photo_image
        '''
        photo_image = photo_image.copy()
        def convert_ratio(img,centerx,centery,wide,height):
            img_wide,img_height = img.shape[1],img.shape[0]
            centerx = centerx * img_wide
            centery = centery * img_height
            startx = centerx - wide*img_wide/2
            starty = centery - height*img_height/2
            return int(startx),int(starty),int(wide*img_wide),int(height*img_height)
        
        def blur_image(img):
            image_blurred = cv2.GaussianBlur(img, (9, 9), 1) 
            # Generate noise with same shape as that of the image
            noise = np.random.normal(0,100, image_blurred.shape) 
            # Add the noise to the image
            img_noised = image_blurred + noise
            img_noised = np.clip(img_noised, 0, 255).astype(np.uint8)
            return img_noised   
        
        def get_blur_image(img,startx,starty,wide,height):
            startx,starty,wide,height = convert_ratio(img,startx,starty,wide,height)
            blured_image = np.copy(img)
            crop_image = img[starty : starty + height , startx : startx + wide]
            crop_image_blurred = blur_image(crop_image)
            blured_image[starty : starty + height , startx : startx + wide] = crop_image_blurred
            return blured_image
        
        for bbb in bounding_box:
            photo_image = get_blur_image(photo_image,bbb[0],bbb[1],bbb[2],bbb[3])

        return photo_image
    
    def predict(self, 
                photo_image):
        '''
        Detect PII card and return the bounding box
        '''
        result = self.__yolo_model(photo_image).xyxyn
        if len(result) == 0:
            return []
        li = []

        for box in result[0]:
            if len(box) == 0:
                continue
            if box[-1] == 1:
                sub_li = []
                x_top = box[0]
                y_top = box[1]
                x_buttom = box[2]
                y_buttom = box[3]
                sub_li.append((x_top+x_buttom)/2)
                sub_li.append((y_top+y_buttom)/2)
                sub_li.append(x_buttom-x_top)
                sub_li.append(y_buttom-y_top)
                li.append(sub_li)
        return li
