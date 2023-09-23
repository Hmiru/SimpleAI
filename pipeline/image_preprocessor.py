'''
불러온 데이터셋으로 전처리를 하는 클래스
'''
from typing import List
from abc import ABC, abstractmethod
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from dataset_maker import *

class Preprocessor(ABC):

    @abstractmethod
    def process(self, train, valid, test):
        pass
class PreProcessing:
    def __init__(self, train_ds, valid_ds, test_ds):
        self.train_ds = train_ds
        self.valid_ds = valid_ds
        self.test_ds = test_ds

        self.preprocess_methods = [Normalizer(), Shuffler(), SquareMaker()]

    def get_dataset_through_preprocessed(self) -> Tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset]:
        for preprocess_method in self.preprocess_methods:
            self.train_ds, self.valid_ds, self.test_ds = preprocess_method.process(self.train_ds, self.valid_ds, self.test_ds)
        return self.train_ds, self.valid_ds, self.test_ds

    def set_preprocess_methods(self, methods: List[Preprocessor]):
        self.preprocess_methods = methods

class SquareMaker(Preprocessor):
    def process(self, train, valid, test):
        train = train.map(self._square_crop)
        valid = valid.map(self._square_crop)
        test = test.map(self._square_crop)
        return train, valid, test

    def _square_crop(self, images, labels):
        # 이미지의 shape 가져오기: (batch_size, height, width, channels)
        shape = tf.shape(images)
        h, w = shape[1], shape[2]

        # 정방형 크기 결정
        s = tf.minimum(h, w)

        # 중앙에서 자를 시작/끝 지점 계산
        y = (h - s) // 2
        x = (w - s) // 2
        cropped_images = images[:, y:y+s, x:x+s, :]

        return cropped_images, labels


class Normalizer(Preprocessor):
    def process(self, train, valid, test):
        normalization_layer = tf.keras.layers.Normalization()
        for images, _ in train:
            normalization_layer.adapt(images)

        train = train.map(lambda x, y: (normalization_layer(x), y))
        valid = valid.map(lambda x, y: (normalization_layer(x), y))
        test = test.map(lambda x, y: (normalization_layer(x), y))
        return train, valid, test

class Shuffler(Preprocessor):
    def process(self, train, valid, test):
        train = train.shuffle(buffer_size=1000).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        valid = valid.shuffle(buffer_size=1000).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        test = test.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        return train, valid, test
