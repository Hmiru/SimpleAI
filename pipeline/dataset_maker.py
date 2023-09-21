'''
데이터셋을 불러와서 Train, valid, test로 분할하는 파일
'''
from typing import Tuple
import tensorflow as tf


class ImageInfo:
    def __init__(self, image_width, image_height):
        self.image_width = image_width
        self.image_height = image_height


class DatasetInfo:
    def __init__(self, train_ratio, valid_ratio, test_ratio, batch_size, seed):
        self.train_ratio = train_ratio
        self.valid_ratio = valid_ratio
        self.test_ratio = test_ratio
        self.batch_size = batch_size
        self.seed = seed

class DatasetLoader:
    def __init__(self, image_path, image_info: ImageInfo, dataset_info: DatasetInfo):
        self.image_path = image_path
        self.image_info = image_info
        self.dataset_info = dataset_info
        self.raw_ds = None
        self.train_ds = None
        self.valid_ds = None
        self.test_ds = None

    def get_datasets(self) -> Tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset]:
        self.__split_dataset_from_directory()
        return self.train_ds, self.valid_ds, self.test_ds

    def __dataset_from_directory(self):
        return tf.keras.preprocessing.image_dataset_from_directory(
            self.image_path,
            image_size=(self.image_info.image_height, self.image_info.image_width),
            seed=self.dataset_info.seed,
            batch_size=self.dataset_info.batch_size,
            label_mode='categorical'
            )

    def __split_dataset_from_directory(self):
        self.raw_ds = self.__dataset_from_directory()
        total_batches = tf.data.experimental.cardinality(self.raw_ds)

        train_batches = int(total_batches.numpy() * self.dataset_info.train_ratio)
        valid_batches = int(total_batches.numpy() * self.dataset_info.valid_ratio)

        self.train_ds = self.raw_ds.take(train_batches)
        self.valid_ds = self.raw_ds.skip(train_batches).take(valid_batches)
        self.test_ds = self.raw_ds.skip(train_batches + valid_batches)


def main():
    dataset_path = "/root/data/images/25k/images"
    image_info = ImageInfo(224, 224)
    dataset_info = DatasetInfo(0.7, 0.2, 0.1, 32, 118)

    loader = DatasetLoader(image_path, image_info, dataset_info)
    train_ds, valid_ds, test_ds = loader.get_datasets()

    print("Number of train batches:", tf.data.experimental.cardinality(train_ds).numpy())
    print("Number of valid batches:", tf.data.experimental.cardinality(valid_ds).numpy())
    print("Number of test batches:", tf.data.experimental.cardinality(test_ds).numpy())

if __name__ == "__main__":
    main()

