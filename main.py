from pre_proc import PreProcessing, ImageInfo, DatasetInfo
from model import build_model
from evaluation import debugging_function
from execution import fit
import sys
class ClassificationModel:
    def __init__(self):
        self.test_ds = None
        self.valid_ds = None
        self.train_ds = None
        self.image_info = ImageInfo(image_height=224, image_width=224)
        self.dataset_info = DatasetInfo(validation_split=0.3, batch_size=32, seed=188)
        self.image_path = "C:\\Users\\mirun\\PycharmProjects\\PhotoTimestamp-AI\\for_vision\\animal_face\\classification_image"


    def preprocess(self):
        preprocessor = PreProcessing(self.image_path, self.image_info, self.dataset_info)
        preprocessor.get_dataset_through_all_procedure()
        self.train_ds = preprocessor.train_ds
        self.valid_ds = preprocessor.valid_ds
        self.test_ds = preprocessor.test_ds

    def train(self):
        model = build_model(base_hidden_units=16, weight_decay=1e-4,input_width=self.image_info.image_width,input_height=self.image_info.image_height)  # 모델 생성하기
        fit(self.train_ds, self.valid_ds, model)
def main():
    clmo = ClassificationModel()
    clmo.preprocess()
    clmo.train()

    if 'debug' in sys.argv:
        print("디버그")
        debugging_function(ClassificationModel.model,ClassificationModel.test_ds)


if __name__ == "__main__":
    main()
    
'''
data_preprocessor.get_ds(data_dir).normalize().shuffle()
train_ds = data_preprocessor.train_ds
valid_ds = data_preprocessor.valid_ds
test_ds = data_preprocessor.test_ds

base_hidden_units = 16  # 은닉층의 유닛수
weight_decay = 1e-4    # L2 규제화 파라미터 Lambda
model=build_model(base_hidden_units, weight_decay)  # 모델 생성하기

study(train_ds, valid_ds,model)
evaluate(model, test_ds)  # 모델 평가하기

img_array = image_input(image_path)  # 사진 입력받기
image_output(model, img_array)  # 사진 결과 출력하기
'''


