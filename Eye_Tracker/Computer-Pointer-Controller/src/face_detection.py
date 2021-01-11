'''
This is a sample class for a model. You may choose to use it as-is or make any changes to it.
This has been provided just to give you an idea of how to structure your model class.
'''

import cv2
import os
import numpy as np
import logging as log
from openvino.inference_engine import IENetwork, IECore


class FaceDetectionModelClass:
    '''
    Class for the Face Detection Model.
    '''

    def __init__(self, model_name, device, threshold, extensions=None):
        '''
        this method is to set instance variables.
        '''
        self.model_weights = model_name + '.bin'
        self.model_structure = model_name + ".xml"
        self.device = device
        self.threshold = threshold
        self.extension = extensions
        self.cropped_face_image = None
        self.first_face_coordinates = None
        self.faces_coordinates = None
        self.results = None
        self.pre_image = None
        self.net = None

        try:
            self.model = IENetwork(self.model_structure, self.model_weights)
        except Exception as e:
            raise ValueError("Check Model Path, Could not Initialise Network")

        self.input_name = next(iter(self.model.inputs))
        self.input_shape = self.model.inputs[self.input_name].shape
        self.output_name = next(iter(self.model.outputs))
        self.output_shape = self.model.outputs[self.output_name].shape

    def load_model(self):
        '''
        This method is for loading the model to the device specified by the user.
        If your model requires any Plugins, this is where you can load them.
        '''
        self.model = IENetwork(self.model_structure, self.model_weights)
        self.core = IECore()
        self.net = self.core.load_network(network=self.model, device_name=self.device, num_requests=1)




    def predict(self, image):
        '''
        This method is meant for running predictions on the input image.
        '''

        self.pre_image = self.preprocess_input(image)
        self.results = self.net.infer({self.input_name: self.pre_image})
        self.faces_coordinates = self.preprocess_output(self.results, image)

        if len(self.faces_coordinates) == 0:
            log.error("No Face is detected, Next frame will be processed..")
            return 0, 0

        self.first_face_coordinates = self.faces_coordinates[0]
        cropped_face_image = image[self.first_face_coordinates[1]:self.first_face_coordinates[3],
                             self.first_face_coordinates[0]:self.first_face_coordinates[2]]

        return self.first_face_coordinates, cropped_face_image

    def check_model(self):
        raise NotImplementedError

    def preprocess_input(self, image):
        '''
        Before feeding the data into the model for inference,
        you might have to preprocess it. This method is where you can do that.
        '''
        frame_pre = cv2.resize(image, (self.input_shape[3], self.input_shape[2]))
        frame_pre = frame_pre.transpose((2, 0, 1))
        frame_pre = frame_pre.reshape(1, *frame_pre.shape)

        return frame_pre

    def preprocess_output(self, outputs, image):
        faces_coordinates = []
        outs = outputs[self.output_name][0][0]
        for box in outs:
            conf = box[2]
            if conf >= self.threshold:
                xmin = int(box[3] * image.shape[1])
                ymin = int(box[4] * image.shape[0])
                xmax = int(box[5] * image.shape[1])
                ymax = int(box[6] * image.shape[0])
                faces_coordinates.append([xmin, ymin, xmax, ymax])
        return faces_coordinates
