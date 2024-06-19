from src.test import Pipeline

def main():
    dataset_path = "/root/data/images/test_daytime"
    classifier = Pipeline(dataset_path)
    classifier.load_datasets()
    classifier.preprocess()
    classifier.model_build(2)
    classifier.compile_fit(20)
    classifier.evaluate_model()


if __name__ == "__main__":
    main()
