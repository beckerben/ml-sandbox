import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Sequential

# Ensure TensorFlow is using the GPU
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Define a large model
model = Sequential([
    Flatten(input_shape=(128, 128, 3)),
    Dense(4096, activation='relu'),
    Dense(4096, activation='relu'),
    Dense(4096, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Generate random data (large dataset)
x_train = tf.random.normal((1000, 128, 128, 3))
y_train = tf.random.uniform((1000,), minval=0, maxval=10, dtype=tf.int32)

# Train the model
model.fit(x_train, y_train, batch_size=64, epochs=5)
 