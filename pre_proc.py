'''
불러온 데이터셋으로 전처리를 하는 클래스
'''
import tensorflow as tf
from data_loader import *

class PreProcessing:
    def __init__(self, train_ds, valid_ds, test_ds):
        self.train_ds = train_ds
        self.valid_ds = valid_ds
        self.test_ds = test_ds
        self.normalization_layer = tf.keras.layers.Normalization()

    def get_dataset_through_preprocessed(self) -> Tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset]:
        self.__normalize()
        self.__shuffle()
        return self.train_ds, self.valid_ds, self.test_ds

    def __normalize(self):
        for images, _ in self.train_ds:
            self.normalization_layer.adapt(images)

        self.train_ds = self.train_ds.map(lambda x, y: (self.normalization_layer(x), y))
        self.valid_ds = self.valid_ds.map(lambda x, y: (self.normalization_layer(x), y))
        self.test_ds = self.test_ds.map(lambda x, y: (self.normalization_layer(x), y))
        return self

    def __shuffle(self):
        self.train_ds = self.train_ds.shuffle(buffer_size=1000).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        self.valid_ds = self.valid_ds.shuffle(buffer_size=1000).prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        self.test_ds = self.test_ds.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
        return self
