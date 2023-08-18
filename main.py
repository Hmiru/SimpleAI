from pre_proc import PreProcessing, ImageInfo, DatasetInfo


def main():

    image_info = ImageInfo(image_height=224, image_width=224) 
    dataset_info = DatasetInfo(validation_split=0.3, batch_size=32, seed=188)
    image_path = "C:/Users/mirun/PycharmProjects/pythonProject/CV/for_vision/animal_face/classification_image"
    preprocessor = PreProcessing(image_path, image_info, dataset_info) # 전처리용 객체 만드는게 이런거?
    preprocessor.get_dataset_through_all_procedure()

    train_ds = preprocessor.train_ds
    valid_ds = preprocessor.valid_ds
    test_ds = preprocessor.test_ds


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


