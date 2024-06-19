'''
파이프라인 클래스를 시작부터 끝까지 이용한 테스트용 파일
'''
from pipeline import Pipeline
import pickle

def main():
    clmo = Pipeline()
    print("학습 모드")
    clmo.image_load()
    clmo.preprocess()
    clmo.config_model()
    trained_model, training_history = clmo.fit(epochs=20)

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
