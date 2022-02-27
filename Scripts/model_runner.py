# Dependencies

import numpy as np
from PIL import Image, ImageOps

import onnxruntime
import json

def predict_emotion(input_buffer):
    model_path = "./Models/facial_emotion_detection.onnx"
    
    # preprocessing
    input_img = Image.open(input_buffer)
    input_img = ImageOps.grayscale(input_img)
    input_img = np.array(input_img.resize((48, 48))) / 1 # Use normalization here

    input_img = np.expand_dims(input_img, axis=0)
    input_img = np.expand_dims(input_img, axis=0)

    input_img = np.reshape(input_img, (1, 48, 48, 1))

    # converting data for onnx model
    data = json.dumps({'data': input_img.tolist()})
    data = np.array(json.loads(data)['data']).astype('float32')

    # starting onnx session and model
    session = onnxruntime.InferenceSession(model_path, None)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name

    # running onnx model
    result = session.run([output_name], {input_name: data})
    return result[0][0]