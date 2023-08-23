'''
이미지 분류과정에 필요한 모든 클래스를 한번에 모아서 만든 프레임워크가 되고싶은 클래스
'''
from pre_proc import PreProcessing, ImageInfo, DatasetInfo
from model import ModelBuilder
from trainer import ModelTrainer
from data_loader import DatasetLoader
import sys
import tensorflow as tf
import yaml

class Pipeline:
    def __init__(self):
        self.test_ds = None
        self.valid_ds = None
        self.train_ds = None
        self.model = None
        self.image_info = ImageInfo(image_height=224, image_width=224)
        with open('config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        handphone_image_path_from_yaml = config['handphone_image_path']
        animal_face_image_path_from_yaml = config['animal_face_image_path']

        self.dataset_info = DatasetInfo(train_ratio=0.8, valid_ratio=0.1, test_ratio=0.1, batch_size=32, seed=188)
        self.image_path = handphone_image_path_from_yaml
        self.dataloader = DatasetLoader(self.image_path, self.image_info, self.dataset_info)

        self.modelbuilder = ModelBuilder(base_hidden_units=16, weight_decay=1e-4, image_info=self.image_info)
        self.modeltrainer = None



    def image_load(self):
        self.train_ds, self.valid_ds, self.test_ds = self.dataloader.get_datasets()
        self.preprocessor = PreProcessing(self.test_ds, self.valid_ds, self.train_ds)

    def preprocess(self):
        self.train_ds, self.valid_ds, self.test_ds = self.preprocessor.get_dataset_through_preprocessed()

    def config_model(self):
        self.model = self.modelbuilder.build()
        self.modeltrainer = ModelTrainer(self.model)

    def fit(self, epochs=15):
        trained_model, training_history = self.modeltrainer.fit(self.train_ds, self.valid_ds, epochs)
        return trained_model, training_history




