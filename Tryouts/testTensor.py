import numpy as np
import tensorflow as tf

# Data
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)  # Y = 2*X

# Model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1]),
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(X, Y, epochs=500)

# Predict
print(model.predict([10.0]))  # It should be close to 20

#[[19.867884]]