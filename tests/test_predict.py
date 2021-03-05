import unittest
import numpy as np
import os
import json
from unittest.mock import patch
from deep_move.predict import get_img_path, get_img, save_prediction
from deep_move.conf import config
from unittest.mock import Mock


class TestPredict(unittest.TestCase):

	@patch('sys.argv', ["exe", "img.png"])
	def test_get_img_path(self):
		config["data_to_predict_path"] = "/tmp/"
		self.assertEqual(
			get_img_path(),
			"/tmp/img.png"
		)

	@patch('deep_move.predict.get_img_path', Mock(return_value="/tests/test_data/img.png"))
	def test_get_img(self):
		img = get_img()
		self.assertEqual(img.shape, (28, 28))

	
	def test_save_prediction(self):
		config["prediction"] = "/tmp/pred"
		save_prediction("img.png", 4)
		exist = os.path.exists(config["prediction"])
		self.assertEqual(exist, True)


	def test_save_prediction_file_content(self):
		
		def get_file_content():
			with open(f'{config["prediction"]}', "r") as json_file:
				data = json.load(json_file)
			return data

		expected = {"img.png": "4"}
		config["prediction"] = "/tmp/pred.json"
		
		save_prediction("img.png", "4")
		data = get_file_content()
		
		self.assertEqual(expected, data)
