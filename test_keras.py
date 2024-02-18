import time
t1=time.time()
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
# Generate some dummy data for training
x_train_data = np.random.random((100, 10))
y_train_data = np.random.randint(2, size=(100, 1))
# Building the model
model = Sequential()
model.add(Dense(10, activation='relu', input_dim=10))
model.add(Dense(1, activation='sigmoid'))
# Compiling the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# Train the model
model.fit(x_train_data, y_train_data, nb_epoch=50, batch_size=5)
# Generate some dummy test data
x_test_data = np.random.random((10, 10))
y_test_data = np.random.randint(2, size=(10, 1))
# Evaluating the model on the test data
loss, accuracy = model.evaluate(x_test_data, y_test_data)
print('Test model loss:', loss)
print('Test model accuracy:', accuracy)
print("Time elapsed:",time.time()-t1)
