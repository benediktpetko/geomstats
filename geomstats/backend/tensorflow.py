"""Tensorflow based computation backend."""

# TODO(johmathe): Reproduce all unit tests with tensorflow backend.

import tensorflow as tf


def abs(x):
    return tf.abs(x)


def zeros(x):
    return tf.zeros(x)


def ones(x):
    return tf.ones(x)


def sin(x):
    return tf.sin(x)


def cos(x):
    return tf.cos(x)


def cosh(x):
    return tf.cosh(x)


def sinh(x):
    return tf.sinh(x)


def tanh(x):
    return tf.tanh(x)


def arccosh(x):
    return tf.arccosh(x)


def tan(x):
    return tf.tan(x)


def arcsin(x):
    return tf.asin(x)


def arccos(x):
    return tf.acos(x)


def shape(x):
    return tf.shape(x)


def ndims(x):
    return x.get_shape()._ndims


def dot(x, y):
    return tf.reduce_sum(tf.multiply(x, y))


def maximum(x, y):
    return tf.maximum(x, y)


def greater_equal(x, y):
    return tf.greater_equal(x, y)


def to_ndarray(x, to_ndim, axis=0):
    if ndims(x) == to_ndim - 1:
        x = tf.expand_dims(x, axis=axis)
    #tf.assert_equal(ndims(x), to_ndim)
    return x


def sqrt(x):
    return tf.sqrt(x)


def isclose(x, y, rtol=1e-05, atol=1e-08):
    rhs = tf.constant(atol) + tf.constant(rtol) * tf.abs(y)
    return tf.less_equal(tf.abs(tf.sub(x, y)), rhs)


def allclose(x, y, rtol=1e-05, atol=1e-08):
    return tf.reduce_all(isclose(x, y, rtol=rtol, atol=atol))


def less_equal(x, y):
    return tf.less_equal(x, y)


def eye(N, M=None):
    return tf.eye(num_rows=N, num_columns=M)


def average(x):
    return tf.reduce_sum(x)


def matmul(x, y):
    return tf.matmul(x, y)


def sum(*args, **kwargs):
    return tf.reduce_sum(*args, **kwargs)


def einsum(equation, *inputs, **kwargs):
    return tf.einsum(equation, *inputs, **kwargs)


def transpose(x):
    return tf.transpose(x)


def squeeze(x):
    return tf.squeeze(x)


def zeros_like(x):
    return tf.zeros_like(x)


def trace(x, **kwargs):
    return tf.trace(x)


def array(x):
    return tf.constant(x)


def all(bool_tensor):
    bool_tensor = tf.cast(bool_tensor, tf.float32)
    all_true = tf.equal(tf.reduce_mean(bool_tensor), 1.0)
    return all_true
