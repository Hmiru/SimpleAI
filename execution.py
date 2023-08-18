from keras.callbacks import ModelCheckpoint
from matplotlib import pyplot
from tensorflow import keras


def fit(train_ds,valid_ds,model):
  batch_size=128
  epochs=15

  checkpointer=ModelCheckpoint(filepath='model.100epochs.hdf5', verbose=1,
                              save_best_only=True)
  optimizer=keras.optimizers.Adam(lr=0.0001,decay=1e-6)

  model.compile(loss='categorical_crossentropy',optimizer=optimizer,
                metrics=['accuracy'])
  history = model.fit(train_ds,
                      batch_size=batch_size,
                      epochs=epochs,
                      verbose=2,
                      validation_data=valid_ds, # 검증 데이터
                      callbacks=[checkpointer])

  pyplot.plot(history.history['accuracy'],label='Train data')
  pyplot.plot(history.history['val_accuracy'],label='Valid data')
  pyplot.legend()
  pyplot.show()

  return model