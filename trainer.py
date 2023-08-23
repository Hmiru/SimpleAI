'''
완성된 모델을 가지고 학습하는 클래스
'''
from keras.callbacks import ModelCheckpoint
from matplotlib import pyplot
from tensorflow import keras
from model import ModelBuilder


class ModelTrainer:
    def __init__(self, model):
        self.model = model
        self.compile()

    def compile(self):
        optimizer = keras.optimizers.legacy.Adam(lr=0.0001, decay=1e-6)
        self.model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    def fit(self, train_ds, valid_ds, epochs):
        checkpointer = ModelCheckpoint(filepath=f'model.{epochs}epochs.hdf5', verbose=1, save_best_only=True)

        history = self.model.fit(train_ds,
                                 batch_size=128,
                                 verbose=2,
                                 epochs=epochs,
                                 validation_data=valid_ds,  # 검증 데이터
                                 callbacks=[checkpointer])
        return self.model, history
