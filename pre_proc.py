import tensorflow as tf


class ImageInfo:
    def __init__(self, image_height, image_width):
        self.image_height = image_height
        self.image_width = image_width


class DatasetInfo:
    def __init__(self, validation_split, batch_size, seed):
        self.validation_split = validation_split
        self.batch_size = batch_size
        self.seed = seed


class PreProcessing:
    def __init__(self, image_path, image_info: ImageInfo, dataset_info: DatasetInfo):
        self.image_path = image_path
        self.image_info = image_info
        self.dataset_info = dataset_info
        self.normalization_layer = tf.keras.layers.Normalization()
        self.train_ds = None
        self.valid_ds = None
        self.test_ds = None

    def __dataset_from_directory_subset(self, subset: str) -> tf.data.Dataset:
        return tf.keras.preprocessing.image_dataset_from_directory(
            self.image_path,
            image_size=(self.image_info.image_height, self.image_info.image_width),
            validation_split=self.dataset_info.validation_split,
            subset=subset,
            seed=self.dataset_info.seed,
            batch_size=self.dataset_info.batch_size,
            label_mode='categorical'
        )

    def __split_dataset_from_directory(self):
        self.train_ds = self.__dataset_from_directory_subset("training")
        self.raw_valid_ds = self.__dataset_from_directory_subset("validation")
        return self

    def get_dataset_through_all_procedure(self) -> tf.data.Dataset:
        self.__split_dataset_from_directory()
        self.__make_test_dataset_from_valid()
        self.__normalize()
        self.__shuffle()

    def __make_test_dataset_from_valid(self):
        valid_batches = tf.data.experimental.cardinality(self.raw_valid_ds)
        self.test_ds = self.raw_valid_ds.take((2*valid_batches) // 3)  # Test set : 20%
        self.valid_ds = self.raw_valid_ds.skip((2*valid_batches) // 3)  # Valid set : 10%
        return self

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
