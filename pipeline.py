'''
이미지 분류과정에 필요한 모든 클래스를 한번에 모아서 만든 프레임워크가 되고싶은 클래스
'''
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
from pre_proc import PreProcessing, ImageInfo, DatasetInfo
from model import ModelBuilder
from trainer import ModelTrainer
from data_loader import DatasetLoader
import sys
import pickle
import tensorflow as tf
from final_test import Debugger
import yaml

class Pipeline:
    def __init__(self):
        self.test_ds = None
        self.valid_ds = None
        self.train_ds = None
        self.model = None
        self.image_info = ImageInfo(image_height=224, image_width=224)
        with open('path_config.yaml', 'r',  encoding='utf-8') as file:
            config = yaml.safe_load(file)
        handphone_image_path_from_yaml = config['handphone_image_path']
        # animal_face_image_path_from_yaml = config['animal_face_image_path']

        self.dataset_info = DatasetInfo(train_ratio=0.8, valid_ratio=0.1, test_ratio=0.1, batch_size=32, seed=188)
        self.image_path = handphone_image_path_from_yaml
        self.dataloader = DatasetLoader(self.image_path, self.image_info, self.dataset_info)

        self.modelbuilder = ModelBuilder(base_hidden_units=16, weight_decay=1e-4, image_info=self.image_info)
        self.modeltrainer = None



    def image_load(self):
        self.train_ds, self.valid_ds, self.test_ds = self.dataloader.get_datasets()
        self.preprocessor = PreProcessing(self.train_ds, self.valid_ds, self.test_ds)

    def preprocess(self,methods=None):
        if methods is None:
            methods = [self.preprocessor.normalize,self.preprocessor.shuffle]
        self.preprocessor.set_preprocess_methods(methods)
        self.train_ds, self.valid_ds, self.test_ds = self.preprocessor.get_dataset_through_preprocessed()
    def config_model(self):
        self.model = self.modelbuilder.build()
        self.modeltrainer = ModelTrainer(self.model)

    def fit(self, epochs=15):
        trained_model, training_history = self.modeltrainer.fit(self.train_ds, self.valid_ds, epochs)
        return trained_model, training_history


def main():
    clmo = Pipeline()
    print("학습 모드")
    clmo.image_load()
    preprocess_methods = [clmo.preprocessor.normalize, clmo.preprocessor.shuffle]
    clmo.preprocess(preprocess_methods)
    clmo.config_model()
    trained_model, training_history = clmo.fit(epochs=10)

    trained_model.save('model.h5')
    with open('training_history.pkl', 'wb') as file:
        pickle.dump(training_history.history, file)
    '''
    training_history.pkl'라는 파일을 바이너리 쓰기 모드('wb')로 연다. 
    열린 파일 객체를 file 변수로 참조.
    pickle.dump 함수는 첫 번째 인자로 주어진 객체를 직렬화하여 두 번째 인자로 주어진 파일 객체에 저장.
    training_history.history 객체를 file에 직렬화하여 저장.
    그나저나 이렇게 쓰면 약간 지저분해지는것 같은데..
    '''

if __name__ == "__main__":
    main()

