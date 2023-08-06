import importlib
import json
import numpy as np
import os
import sys
import time
import uuid
import copy

from hypergan.discriminators import *
from hypergan.encoders import *
from hypergan.generators import *
from hypergan.inputs import *
from hypergan.samplers import *
from hypergan.trainers import *

import hyperchamber as hc
from hyperchamber import Config
from hypergan.ops import TensorflowOps
import tensorflow as tf
import hypergan as hg

from hypergan.gan_component import ValidationException, GANComponent
from .base_gan import BaseGAN

from hypergan.discriminators.fully_connected_discriminator import FullyConnectedDiscriminator
from hypergan.encoders.uniform_encoder import UniformEncoder
from hypergan.trainers.multi_step_trainer import MultiStepTrainer

class AlignedAlphaGAN(BaseGAN):
    """ 
    """
    def __init__(self, *args, **kwargs):
        BaseGAN.__init__(self, *args, **kwargs)
        self.discriminator = None
        self.encoder = None
        self.generator = None
        self.loss = None
        self.trainer = None
        self.session = None


    def required(self):
        return "generator".split()

    def create(self):
        BaseGAN.create(self)
        if self.session is None: 
            self.session = self.ops.new_session(self.ops_config)
        with tf.device(self.device):
            config = self.config
            ops = self.ops

            d2 = dict(config.discriminator)
            d2['class'] = self.ops.lookup("class:hypergan.discriminators.pyramid_discriminator.PyramidDiscriminator")

            encoder_xab = self.create_component(d2)
            encoder_xab.ops.describe("encoder_xa")
            encoder_xab.create(self.inputs.xa)
            encoder_xab.z = tf.zeros(0)

            encoder_xba = self.create_component(d2)
            encoder_xba.ops.describe("encoder_xb")
            encoder_xba.create(self.inputs.xb)
            encoder_xba.z = tf.zeros(0)

            d3 = dict(config.discriminator)
            d3["layers"]=config.discriminator.encoder_layers or 3
            d3["fc_layers"]=0

            encoder_discriminator = self.create_component(d3)
            #encoder_discriminator = FullyConnectedDiscriminator(self, {})
            encoder_discriminator.ops.describe("encoder_discriminator")
            standard_discriminator = self.create_component(config.discriminator)
            standard_discriminator.ops.describe("discriminator")

            #encoder.sample = ops.reshape(encoder.sample, [ops.shape(encoder.sample)[0], -1])
            uniform_encoder_config = config.encoder
            z_size = 1
            for size in ops.shape(encoder_xba.sample)[1:]:
                z_size *= size
            uniform_encoder_config.z = z_size//len(uniform_encoder_config.projections)
            uniform_encoder = UniformEncoder(self, uniform_encoder_config)
            uniform_encoder.create()

            self.generator = self.create_component(config.generator)

            za = uniform_encoder.sample
            za = ops.reshape(za, ops.shape(encoder_xba.sample))
            xa = self.inputs.xa
            xb = self.inputs.xb
            za_hat = encoder_xba.sample
            zb_hat = encoder_xab.sample

            d4 = dict(d3)
            d4['layers'] = 0
            d4['extra_layers'] = 3
            z_encoder = self.create_component(d4)
            #encoder_discriminator = FullyConnectedDiscriminator(self, {})
            z_encoder.ops.describe("z_encoder")

            zaba_hat = z_encoder.create(za_hat)

            zbab_hat = z_encoder.reuse(zb_hat)
            print("ZA", za_hat, zaba_hat, zbab_hat, za)
            zb = z_encoder.reuse(za)

            g = self.generator.create(za)
            g2 = self.generator.reuse(zb)
            sample = g
            xab = self.generator.reuse(zb_hat)
            xba = self.generator.reuse(za_hat)
            xa_hat = self.generator.reuse(zaba_hat)
            reconstruction = xa_hat
            xb_hat = self.generator.reuse(zbab_hat)

            ed_net = ops.concat([za, zaba_hat, zbab_hat], axis=0)
            encoder_discriminator.create(ed_net)

            eloss = dict(config.loss)
            eloss['gradient_penalty'] = False
            encoder_loss = self.create_component(eloss, discriminator = encoder_discriminator)
            encoder_loss.create(split=3)

            stacked_xg = ops.concat([xa, xb, xa_hat, xb_hat, g, g2], axis=0)
            standard_discriminator.create(stacked_xg)

            standard_loss = self.create_component(config.loss, discriminator = standard_discriminator)
            standard_loss.create(split=6)

            self.trainer = self.create_component(config.trainer)

            #loss terms
            distance = config.distance or ops.lookup('l1_distance')
            cycloss = tf.reduce_mean(tf.abs(distance(self.inputs.xa,xa_hat)))
            cycloss += tf.reduce_mean(tf.abs(distance(self.inputs.xb,xb_hat)))
            cycloss_lambda = config.cycloss_lambda or 10
            cycloss *= cycloss_lambda
            loss1=('generator', cycloss + encoder_loss.g_loss)
            loss2=('generator', cycloss + standard_loss.g_loss)
            loss3=('discriminator', standard_loss.d_loss)
            loss4=('discriminator', encoder_loss.d_loss)

            var_lists = []
            var_lists.append(encoder_xab.variables() + encoder_xba.variables())
            var_lists.append(self.generator.variables())
            var_lists.append(standard_discriminator.variables())
            var_lists.append(encoder_discriminator.variables())

            metrics = []
            metrics.append(encoder_loss.metrics)
            metrics.append(standard_loss.metrics)
            metrics.append(None)
            metrics.append(None)

            # trainer

            self.trainer = MultiStepTrainer(self, self.config.trainer, [loss1,loss2,loss3,loss4], var_lists=var_lists, metrics=metrics)
            self.trainer.create()

            self.session.run(tf.global_variables_initializer())

            #self.generator.sample = sample
            self.generator.reconstruction = reconstruction
            self.encoder = encoder_xab
            self.uniform_encoder = uniform_encoder

            self.cyca = xa_hat
            self.cycb = xb_hat
            self.xba = xba
            self.xab = xab


    def step(self, feed_dict={}):
        return self.trainer.step(feed_dict)
