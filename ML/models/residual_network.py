import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, Rescaling, Input, Add, Activation, BatchNormalization
# Dense, Flatten, Conv2D, MaxPooling2D, Dropout, Rescaling, Input, Add, Activation, BatchNormalization, AveragePooling2D

def conv_bn_ac_block(input_tensor, filters, kernel_size, strides=(1, 1), padding='same', activation='relu', name=, **kwargs):
    if kwargs['name']:
        name = kwargs['name']

    x = Conv2D(filters, kernel_size, strides=strides, padding=padding, weight_decay=1e-4, **kwargs)(input_tensor)
    x = BatchNormalization()(x)
    x = Activation(activation)(x)
    return x

