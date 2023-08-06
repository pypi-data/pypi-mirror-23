# -*- coding: utf-8 -*-

"""

keras_resnet.blocks._3d
~~~~~~~~~~~~~~~~~~~~~~~

This module implements a number of popular three-dimensional residual blocks.

"""

import keras.layers
import keras.regularizers

parameters = {
    "kernel_initializer": "he_normal"
}


def basic_3d(filters, strides=(1, 1), first=False):
    """

    A three-dimensional basic block.

    :param filters: the output’s feature space

    :param strides: the convolution’s stride

    :param first: whether this is the first instance inside a residual block

    Usage:

        >>> import keras_resnet.blocks

        >>> keras_resnet.blocks.basic_3d(64)

    """
    def f(x):
        if keras.backend.image_data_format() == "channels_last":
            axis = 3
        else:
            axis = 1

        y = keras.layers.Conv3D(filters, (3, 3, 3), strides=strides, padding="same", **parameters)(x)

        y = keras.layers.BatchNormalization(axis=axis)(y)
        y = keras.layers.Activation("relu")(y)

        y = keras.layers.Conv3D(filters, (3, 3, 3), padding="same", **parameters)(y)

        y = keras.layers.BatchNormalization(axis=axis)(y)
        y = _shortcut(x, y)
        y = keras.layers.Activation("relu")(y)

        return y

    return f


def bottleneck_3d(filters, strides=(1, 1), first=False):
    """

    A three-dimensional bottleneck block.

    :param filters: the output’s feature space

    :param strides: the convolution’s stride

    :param first: whether this is the first instance inside a residual block

    Usage:

        >>> import keras_resnet.blocks

        >>> keras_resnet.blocks.bottleneck_3d(64)

    """
    def f(x):
        if keras.backend.image_data_format() == "channels_last":
            axis = 3
        else:
            axis = 1

        if first:
            y = keras.layers.Conv3D(filters, (1, 1, 1), strides=strides, padding="same", **parameters)(x)
        else:
            y = keras.layers.Conv3D(filters, (3, 3, 3), strides=strides, padding="same", **parameters)(x)

        y = keras.layers.BatchNormalization(axis=axis)(y)
        y = keras.layers.Activation("relu")(y)

        y = keras.layers.Conv3D(filters, (3, 3, 3), padding="same", **parameters)(y)

        y = keras.layers.BatchNormalization(axis=axis)(y)
        y = keras.layers.Activation("relu")(y)

        y = keras.layers.Conv3D(filters * 4, (1, 1, 1), **parameters)(y)

        y = keras.layers.BatchNormalization(axis=axis)(y)
        y = _shortcut(x, y)
        y = keras.layers.Activation("relu")(y)

        return y

    return f


def _shortcut(a, b):
    a_shape = keras.backend.int_shape(a)
    b_shape = keras.backend.int_shape(b)

    if keras.backend.image_data_format() == "channels_last":
        x = int(round(a_shape[1] / b_shape[1]))
        y = int(round(a_shape[2] / b_shape[2]))

        if x > 1 or y > 1 or not a_shape[3] == b_shape[3]:
            a = keras.layers.Conv3D(b_shape[3], (1, 1, 1), strides=(x, y), padding="same", **parameters)(a)

            a = keras.layers.BatchNormalization(axis=3)(a)
    else:
        x = int(round(a_shape[2] / b_shape[2]))
        y = int(round(a_shape[3] / b_shape[3]))

        if x > 1 or y > 1 or not a_shape[1] == b_shape[1]:
            a = keras.layers.Conv3D(b_shape[1], (1, 1, 1), strides=(x, y), padding="same", **parameters)(a)

            a = keras.layers.BatchNormalization(axis=1)(a)

    return keras.layers.add([a, b])
