from model_provider import BaseModel
from tensorflow.keras.applications import vgg16
from tensorflow.keras.layers import Flatten, Dense, BatchNormalization, Dropout
from tensorflow.keras.models import Model

class straight_vgg16(BaseModel):
    def __init__(self, image_info):
        self.input_width = image_info.image_width
        self.input_height = image_info.image_height
    def build(self,output):
        '''그대로 신경망'''
        base_model = vgg16.VGG16(weights="imagenet", include_top=False, input_shape=( self.input_width,self.input_height,3))
        
        for layer in base_model.layers:
            layer.trainable=False
        
        last_layer=base_model.get_layer('block5_pool')
        last_output=last_layer.output
        x=Flatten()(last_output)
        
        x=Dense(64, activation='relu', name='FC_2')(x)
        x=BatchNormalization()(x)
        x=Dropout(0.5)(x)
        x=Dense(output, activation='softmax', name='softmax')(x)
        
        model = Model(inputs=base_model.input, outputs=x)
        model.summary()


        return model