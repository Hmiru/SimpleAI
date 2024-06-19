
from PIL import Image


from PIL import Image
import numpy as np

import io
#from image_preprocessor import SquareMaker, Normalizer
import tensorflow as tf
from keras_preprocessing.image import img_to_array


class seasonEstimator:

    def load_model(self):

        global model
        model = tf.keras.models.load_model('pipeline/weight/season_predictor_with_20epochs.hdf5')
def input(image, target):
    # 만약 이미지가 RGB가 아니라면, RGB로 변환해줍니다.
    if image.mode != "RGB":
        image = image.convert("RGB")

    # 입력 이미지 사이즈를 재정의하고 사전 처리를 진행합니다.
    square_maker = SquareMaker()
    preprocessor=Normalizer()
    image=square_maker._square_crop(image)
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image=preprocessor.normalization_layer(image)
    return image
def output():
    pass
def main():
    image_path="C:/Users/mirun/image_dataset/photo_timestamp/real/korea_Phototimestamp_ds/Spring_Afternoon"
    img=Image.open(image_path)
    print(img.info())
    img_modified=input(img,(224,224))
    img_modified.info()
if __name__=="__main__":
    main(0)
