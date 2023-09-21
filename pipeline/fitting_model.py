'''
완성된 모델을 가지고 학습하는 클래스
'''
from keras.callbacks import ModelCheckpoint

from tensorflow import keras
from model_making import New_Model
import tensorflow as tf

class ModelTrainer:
    def __init__(self, model):
        self.model = model
        #self.compile()

    def compile(self):
        optimizer = optimizer = keras.optimizers.legacy.Adam(learning_rate=0.0001, decay=1e-6)
        self.model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    def fit(self, train_ds, valid_ds, epochs):
        checkpointer = ModelCheckpoint(filepath=f'/root/data/code-space/PhotoTimestamp-AI/model_storage/nature_divide_model.{epochs}epochs.hdf5', verbose=1, save_best_only=True)
        reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                                                          patience=5, min_lr=0.0001)
        history = self.model.fit(train_ds,
                                 batch_size=128,
                                 verbose=2,
                                 epochs=epochs,
                                 validation_data=valid_ds,  # 검증 데이터
                                 callbacks=[checkpointer, reduce_lr])
        return self.model, history

    def evaluate(self,test_ds):
        return self.model.evaluate(test_ds)