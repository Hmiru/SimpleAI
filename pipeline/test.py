from image_preprocessor import PreProcessing
from dataset_maker import DatasetLoader, ImageInfo, DatasetInfo
from model_making import New_Model
from fitting_model import ModelTrainer
import tensorflow as tf
from VGG_16 import straight_vgg16
class Pipeline:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_info = ImageInfo(224, 224)
        self.dataset_info = DatasetInfo(0.7, 0.2, 0.1, 16, 118)
        self.dataloader = DatasetLoader(self.image_path, self.image_info, self.dataset_info)
        self.new_model_maker = New_Model(image_info=self.image_info)
        self.train_ds = None
        self.valid_ds = None
        self.test_ds = None
        self.preprocessor = None
        self.model = None
        self.modeltrainer = None 

    def load_datasets(self):
        self.train_ds, self.valid_ds, self.test_ds = self.dataloader.get_datasets()
        self.preprocessor = PreProcessing(self.train_ds, self.valid_ds, self.test_ds)

    def preprocess(self, methods=None):        
        self.train_ds, self.valid_ds, self.test_ds = self.preprocessor.get_dataset_through_preprocessed()
        sample_images, sample_labels = next(iter(self.train_ds))
        print(sample_labels.shape)

    def model_build(self,output):

        self.model=self.new_model_maker.build(output)
        self.modeltrainer = ModelTrainer(self.model)

    def compile_fit(self, epochs=15):
        self.modeltrainer.compile()
        trained_model, training_history = self.modeltrainer.fit(self.train_ds, self.valid_ds, epochs)
        return trained_model, training_history

    def evaluate_model(self):
        '''메인 모델에 대한 평가'''
        loss, accuracy = self.modeltrainer.evaluate(self.test_ds)
        print(f"Test Loss: {loss}")
        print(f"Test Accuracy: {accuracy}")
        return loss, accuracy
        


def main():
    dataset_path = "/root/data/images/test_daytime"
    classifier = Pipeline(dataset_path)
    classifier.load_datasets()
    classifier.preprocess()
#     sample_images, sample_labels = next(iter(classifier.train_ds))

# # 레이블의 형태 출력
#     print(sample_labels.shape)
    classifier.model_build(2)
    classifier.compile_fit(20)
    classifier.evaluate_model()

if __name__ == "__main__":
    main()


