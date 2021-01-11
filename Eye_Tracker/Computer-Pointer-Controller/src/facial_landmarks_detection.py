'''
This is a sample class for a model. You may choose to use it as-is or make any changes to it.
This has been provided just to give you an idea of how to structure your model class.
'''

import cv2
import numpy as np
import logging as log
from openvino.inference_engine import IENetwork, IECore


class FacialLandmarksModelClass:
    '''
    Class for the Facial Landmarks Model.
    '''

    def __init__(self, model_name, device, extensions=None):
        '''
        this method is to set instance variables.
        '''
        self.model_weights = model_name + '.bin'
        self.model_structure = model_name + '.xml'
        self.device = device
        self.extension = extensions

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
        self.img = self.preprocess_input(image)
        input_dict = {self.input_name:self.img}
        self.results = self.net.infer(input_dict)
        
        self.output = self.preprocess_output(self.results, image)

        left_eye_x_min = self.output['left_eye_x'] - 5
        left_eye_x_max = self.output['left_eye_x'] + 5
        left_eye_y_min = self.output['left_eye_y'] - 5
        left_eye_y_max = self.output['left_eye_y'] + 5

        right_eye_x_min = self.output['right_eye_x'] - 5
        right_eye_x_max = self.output['right_eye_x'] + 5
        right_eye_y_min = self.output['right_eye_y'] - 5
        right_eye_y_max = self.output['right_eye_y'] + 5

        self.eye_coords = [[left_eye_x_min, left_eye_y_min, left_eye_x_max, left_eye_y_max],
                          [right_eye_x_min, right_eye_y_min, right_eye_x_max, right_eye_y_max]]
        left_eye_image = image[left_eye_x_min:left_eye_x_max, left_eye_y_min:left_eye_y_max]
        right_eye_image = image[right_eye_x_min:right_eye_x_max, right_eye_y_min:right_eye_y_max]

        return left_eye_image, right_eye_image, self.eye_coords

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
        '''
        Before feeding the output of this model to the next model,
        you might have to preprocess the output. This function is where you can do that.
        '''

       
        outs = outputs[self.output_name][0]
        left_eye_x = int(outs[0] * image.shape[1])
        left_eye_y = int(outs[1] * image.shape[0])
        right_eye_x = int(outs[2] * image.shape[1])
        right_eye_y = int(outs[3] * image.shape[0])

        return {'left_eye_x': left_eye_x, 'left_eye_y': left_eye_y,
                'right_eye_x': right_eye_x, 'right_eye_y': right_eye_y}
