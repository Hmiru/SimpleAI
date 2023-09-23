
from keras.preprocessing.image import load_img

from keras import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization, Conv2D, MaxPooling2D
from keras import regularizers
from keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications import imagenet_utils
from tensorflow.keras.applications import vgg16
from keras.applications import mobilenet
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam, SGD
from keras.metrics import categorical_crossentropy
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input

import itertools

from tensorflow import keras



from keras.preprocessing.image import load_img

from keras import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization, Conv2D, MaxPooling2D
from keras import regularizers
from keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.applications import imagenet_utils
from tensorflow.keras.applications import vgg16
from keras.applications import mobilenet
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.optimizers import Adam, SGD
from keras.metrics import categorical_crossentropy
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input

import itertools

from tensorflow import keras
import sys
sys.path.append('/root/data/code-space/PhotoTimestamp-AI/pipeline/model_wiki')
from VGG_16 import straight_vgg16 
from VGG16_fine_tuned import tuning_vgg16

class New_Model:
    def __init__(self, image_info):
        self.input_width = image_info.image_width
        self.input_height = image_info.image_height
        self.straight_vgg_model = straight_vgg16(image_info)  
        self.tuned_vgg_model = tuning_vgg16(image_info)

    def build(self,output):
        return self.tuned_vgg_model.build(output)  





def main():
    pass


if __name__=="__main__":
    main()





def main():
    pass


if __name__=="__main__":
    main()
