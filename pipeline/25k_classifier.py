from src.test import Pipeline

def main():
    dataset_path = "C:/Users/mirun/image_dataset/photo_timestamp/real/korea_Phototimestamp_ds"
    classifier = Pipeline(dataset_path)
    classifier.load_datasets()
    classifier.preprocess()
    classifier.model_build(12)
    classifier.compile_fit(20)
    classifier.evaluate_model()


if __name__ == "__main__":
    main()
