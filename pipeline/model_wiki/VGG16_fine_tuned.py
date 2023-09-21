from model_provider import BaseModel
from tensorflow.keras.layers import Flatten, Dense, BatchNormalization, Dropout
from tensorflow.keras.applications import vgg16
from tensorflow.keras.models import Model
class tuning_vgg16(BaseModel):
    def __init__(self, image_info):
        self.input_width = image_info.image_width
        self.input_height = image_info.image_height
    def build(self,output):  
        '''파인 튜닝'''
        base_model = vgg16.VGG16(weights="imagenet", include_top=False, input_shape=(self.input_width,self.input_height,3), pooling='avg')

        for layer in base_model.layers[:-5]:
            layer.trainable=False

        last_output=base_model.output
        x=Dense(output, activation='softmax', name='softmax')(last_output)
        model=Model(inputs=base_model.input, outputs=x)
        return model