from keras import Sequential
from keras.layers import Dense,Activation,Flatten,Dropout,BatchNormalization,Conv2D,MaxPooling2D
from keras import regularizers

def build_model(base_hidden_units, weight_decay,input_width,input_height):

  model=Sequential() #(차례대로 층을 추가하는)순차형 모델 초기화

  #conv1
  model.add(Conv2D(base_hidden_units, kernel_size=3, padding='same',
                  kernel_regularizer=regularizers.l2(weight_decay),input_shape=(input_width,input_height,3)))
  model.add(Activation('relu'))

  #conv2
  model.add(Conv2D(base_hidden_units, kernel_size=3, padding='same',
                  kernel_regularizer=regularizers.l2(weight_decay)))
  model.add(Activation('relu'))

  #POOL1
  model.add(MaxPooling2D(pool_size=(2,2)))
  model.add(Dropout(0.3))

  #conv3
  model.add(Conv2D(base_hidden_units*2, kernel_size=3, padding='same',
                  kernel_regularizer=regularizers.l2(weight_decay)))
  model.add(Activation('relu'))

  #conv4
  model.add(Conv2D(base_hidden_units*2, kernel_size=3, padding='same',
                  kernel_regularizer=regularizers.l2(weight_decay)))
  model.add(Activation('relu'))

  #POOL2
  model.add(MaxPooling2D(pool_size=(2,2)))

  #conv5
  model.add(Conv2D(base_hidden_units*4, kernel_size=3, padding='same',
                  kernel_regularizer=regularizers.l2(weight_decay)))
  model.add(Activation('relu'))

  #conv6
  model.add(Conv2D(base_hidden_units*4, kernel_size=3, padding='same',
                  kernel_regularizer=regularizers.l2(weight_decay)))
  model.add(Activation('relu'))

  #POOL3
  model.add(MaxPooling2D(pool_size=(2,2)))
  model.add(Dropout(0.4))

  #FC1
  model.add(Flatten())

  model.add(Dense(100,activation='relu'))

  #FC2
  model.add(Dense(4,activation='softmax'))

  model.summary()

  return model