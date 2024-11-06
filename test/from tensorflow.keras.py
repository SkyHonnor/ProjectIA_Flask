from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

num_train = X_train.shape[0]
num_test = X_test.shape[0]

img_height = X_train.shape[1]
img_width = X_train.shape[2]

# Reshape data
X_train = X_train.reshape((num_train, img_height * img_width))
X_test = X_test.reshape((num_test, img_height * img_width))

# Encode labels
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

from tensorflow.keras import Input
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.models import Model

# Define model
num_classes = 10
xi = Input(shape=(img_height * img_width,))  # Input layer
x = Dense(128, activation='sigmoid')(xi)  # First hidden layer with 128 neurons
x = Dense(64, activation='sigmoid')(x)    # Second hidden layer with 64 neurons
x = Dense(32, activation='sigmoid')(x)    # Third hidden layer with 32 neurons
y = Dense(num_classes, activation='softmax')(x)  # Output layer with 10 neurons (for 10 classes)

# Create the model
model = Model(inputs=[xi], outputs=[y])


# Print model summary
model.summary()  # 7,850 parameters

# Compile model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Fit model
model.fit(X_train, y_train,
          batch_size=128,
          epochs=20,
          verbose=1,
          validation_split=0.1)

# Test model
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
