#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x538c9a03

# Compiled with Coconut version 1.2.3-post_dev1 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

import tensorflow as tf

#####################################
# batch_norm
#####################################

def dense_batch_norm(*args, **kwargs):

    name = kwargs.pop("name", None)
    activation = kwargs.pop("activation", None)
    batch_norm = kwargs.pop("batch_norm", {})

    with tf.variable_scope(name, "DenseBatchNorm"):
        net = tf.layers.dense(*args, **kwargs)
        net = tf.layers.batch_normalization(net, **batch_norm)

        return activation(net) if activation else net

def conv2d_batch_norm(*args, **kwargs):

    name = kwargs.pop("name", None)
    activation = kwargs.pop("activation", None)
    batch_norm = kwargs.pop("batch_norm", {})

    with tf.variable_scope(name, default_name="Conv2dBatchNorm"):
        net = tf.layers.conv2d(*args, **kwargs)
        net = tf.layers.batch_normalization(net, **batch_norm)

        return activation(net) if activation else net

#####################################
# fire
#####################################
def fire(inputs, squeeze_filters, expand_1x1_filters, expand_3x3_filters, **kwargs):

    name = kwargs.pop("name", None)

    with tf.variable_scope(name, default_name="Fire"):
# squeeze
        squeeze = tf.layers.conv2d(inputs, squeeze_filters, [1, 1], **kwargs)

# expand
        kwargs["padding"] = "same"
        expand_1x1 = tf.layers.conv2d(squeeze, expand_1x1_filters, [1, 1], **kwargs)
        expand_3x3 = tf.layers.conv2d(squeeze, expand_3x3_filters, [3, 3], **kwargs)

        return tf.concat([expand_1x1, expand_3x3], axis=3)


def fire_batch_norm(inputs, squeeze_filters, expand_1x1_filters, expand_3x3_filters, **kwargs):

    name = kwargs.pop("name", None)

    with tf.variable_scope(name, default_name="FireBatchNorm"):
# squeeze
        squeeze = conv2d_batch_norm(inputs, squeeze_filters, [1, 1], **kwargs)

# expand
        kwargs["padding"] = "same"
        expand_1x1 = conv2d_batch_norm(squeeze, expand_1x1_filters, [1, 1], **kwargs)
        expand_3x3 = conv2d_batch_norm(squeeze, expand_3x3_filters, [3, 3], **kwargs)

        return tf.concat([expand_1x1, expand_3x3], axis=3)


#####################################
# dense_block
#####################################

def conv2d_densenet_layer(net, growth_rate, bottleneck, batch_norm, dropout, activation, **kwargs):

    with tf.variable_scope(None, default_name="Conv2dDenseNetlayer"):

        net = tf.layers.batch_normalization(net, **batch_norm)
        net = activation(net) if activation else net

        if bottleneck:
            net = tf.layers.conv2d(net, bottleneck, [1, 1], **kwargs)
            net = tf.layers.dropout(net, **dropout)
            net = tf.layers.batch_normalization(net, **batch_norm)
            net = activation(net) if activation else net

        net = tf.layers.conv2d(net, growth_rate, [3, 3], **kwargs)
        net = tf.layers.dropout(net, **dropout)

        return net


def conv2d_densenet_transition(net, compression, batch_norm, dropout, activation, **kwargs):

    filters = int(net.get_shape()[-1])

    if compression:
        if compression <= 1:
            filters = int(filters * compression)
        else:
            filters = compression

    with tf.variable_scope(None, default_name="TransitionLayer"):

        net = tf.layers.batch_normalization(net, **batch_norm)
        net = activation(net) if activation else net
        net = tf.layers.conv2d(net, filters, [1, 1], **kwargs)
        net = tf.layers.dropout(net, **dropout)

        return net


def conv2d_dense_block(net, growth_rate, n_layers, **kwargs):
    name = kwargs.pop("name", None)
    bottleneck = kwargs.pop("bottleneck", None)
    compression = kwargs.pop("compression", None)
    batch_norm = kwargs.pop("batch_norm", {})
    dropout = kwargs.pop("dropout", {})
    activation = kwargs.pop("activation")

    with tf.variable_scope(name, default_name="Conv2dDenseNetBlock"):

        for layers in range(n_layers):
            layer = conv2d_densenet_layer(net, growth_rate, bottleneck, batch_norm, dropout, activation, **kwargs)
            net = tf.concat([net, layer], axis=3)

        net = conv2d_densenet_transition(net, compression, batch_norm, dropout, activation, **kwargs)

    return net

#####################################
# densefire_block
#####################################

def conv2d_densefire_layer(net, bottleneck, growth_rate_1x1, growth_rate_3x3, batch_norm, dropout, activation, **kwargs):

    with tf.variable_scope(None, default_name="Conv2dDenseFireLayer"):

        net = tf.layers.batch_normalization(net, **batch_norm)
        net = activation(net) if activation else net

# squeeze
        net = tf.layers.conv2d(net, bottleneck, [1, 1], **kwargs)
        net = tf.layers.dropout(net, **dropout)
        net = tf.layers.batch_normalization(net, **batch_norm)
        net = activation(net) if activation else net

# expand
        expand_1x1 = tf.layers.conv2d(net, growth_rate_1x1, [1, 1], **kwargs)
        expand_3x3 = tf.layers.conv2d(net, growth_rate_3x3, [3, 3], **kwargs)

# concat
        net = tf.concat([expand_1x1, expand_3x3], axis=3)
        net = tf.layers.dropout(net, **dropout)

        return net



def conv2d_densefire_block(net, bottleneck, growth_rate_1x1, growth_rate_3x3, n_layers, **kwargs):
    name = kwargs.pop("name", None)
    compression = kwargs.pop("compression", None)
    batch_norm = kwargs.pop("batch_norm", {})
    dropout = kwargs.pop("dropout", {})
    activation = kwargs.pop("activation")

    with tf.variable_scope(name, default_name="Conv2dDenseFireBlock"):

        for layers in range(n_layers):
            layer = conv2d_densefire_layer(net, bottleneck, growth_rate_1x1, growth_rate_3x3, batch_norm, dropout, activation, **kwargs)
            net = tf.concat([net, layer], axis=3)

        net = conv2d_densenet_transition(net, compression, batch_norm, dropout, activation, **kwargs)

    return net


#####################################
# ensemble_dropout
#####################################

def layer_dropout(net, **kwargs):

    name = kwargs.pop("name", None)

    with tf.name_scope(name, default_name="LayerDropout"):
        shape = tf.shape(net)
        batche_size = shape[0]
        ones_shape = [batche_size] + ([1] * (len(net.get_shape()) - 1))
        ones = tf.ones(shape=ones_shape)

        return net * tf.layers.dropout(ones, **kwargs)

def ensemble_dropout(networks, **kwargs):

    return (list)((_coconut.functools.partial(map, _coconut_partial(layer_dropout, {}, 1, **kwargs)))(networks))


if __name__ == '__main__':

    sess = tf.Session()

    training = tf.placeholder(tf.bool, shape=())
    x = tf.random_uniform(shape=(16, 3, 2))


# f = fire(x, 32, 64, 64, activation=tf.nn.relu)
# fb = fire_batch_norm(x, 32, 64, 64, activation=tf.nn.relu, batch_norm=dict(training=True))
# print(f)
# print(fb)

    e = ensemble_dropout([x], rate=0.5, training=training)

    print(e)
    print(sess.run(e, feed_dict={training: True}))
