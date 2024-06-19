'''
완료된 모델과 테스트셋으로 최종 평가를 하고, Trian과 Valid의 학습과정에서 정확도를 그래프로 나타내는 클래스
'''
from final_test import Debugger
import pickle
from tensorflow import keras
from pipeline import Pipeline


def main():
    print("디버그 모드")
    loaded_model = keras.models.load_model('model.h5')
    with open('training_history.pkl', 'rb') as file:
        loaded_history = pickle.load(file)


    Debugger.draw_training_history(loaded_history)
    #Debugger.check_test_performance(loaded_model, clmo.test_ds)
    #test_ds받아오는게 의문


if __name__ == "__main__":
    main()