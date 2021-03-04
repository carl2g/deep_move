import sys
import os
import numpy as np
import json
from model import load_model
from skimage import io
from conf import config


def get_img_path() -> str:
	'''
		Return the absolute path of the image to predict 
	'''
	return 	os.path.join(
		config["data_to_predict_path"], 
		sys.argv[1]
	)


def get_img() -> np.ndarray:
	'''
		Return the image as a np.ndarray 
	'''
	return io.imread(
		get_img_path()
	)


def save_prediction(image_name: str, pred: str):
	'''
		Parameters: 
			image_name (str): name of the file of the prediction
			pred (str): the predicted class for the image
	'''
	pred_info = {
		f"{image_name}": f"{pred}"
	}

	with open(config["prediction"], 'w+') as file:
		json.dump(pred_info, file)


if __name__ == "__main__":
	model = load_model()
	img = get_img()
	pred = model.predict(np.reshape(img, (1, 28, 28)))[0]
	save_prediction(sys.argv[1], pred)
