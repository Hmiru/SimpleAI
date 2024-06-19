'''
불러온 데이터셋으로 전처리를 하는 클래스
'''
from typing import List

import tensorflow as tf

from data_loader import *

class PreProcessing:
    def __init__(self, train_ds, valid_ds, test_ds):
        self.train_ds = train_ds
        self.valid_ds = valid_ds
        self.test_ds = test_ds

        self.preprocess_methods = [self.normalize, self.shuffle]

    def get_dataset_through_preprocessed(self) -> Tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset]:
        for preprocess_method in self.preprocess_methods:
            self.train_ds, self.valid_ds, self.test_ds = preprocess_method(self.train_ds, self.valid_ds, self.test_ds)
        return self.train_ds, self.valid_ds, self.test_ds

    def normalize(self, train, valid, test):
        normalization_layer = tf.keras.layers.Normalization()
        for images, _ in train:
            normalization_layer.adapt(images)

        train = train.map(lambda x, y: (normalization_layer(x), y))
        valid = valid.map(lambda x, y: (normalization_layer(x), y))
        test = test.map(lambda x, y: (normalization_layer(x), y))
        return train, valid, test

    def shuffle(self, train , valid, test):
        train = train.shuffle(buffer_size=1000).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        valid = valid.shuffle(buffer_size=1000).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        test = test.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        return train, valid, test

    def set_preprocess_methods(self, methods: List[callable]):
        self.preprocess_methods = methods
