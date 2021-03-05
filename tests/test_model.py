import unittest
import os
from deep_move.model import save_model
from deep_move.conf import config
from sklearn.neural_network import MLPClassifier

class TestModel(unittest.TestCase):

	def test_save_model(self):

		def save_new_model():
			model = MLPClassifier()
			save_model(model)
		
		def test_new_model_saving():
			exist = os.path.exists(config["model_path"])
			self.assertEqual(exist, True)
		
		config["model_path"] = "/tmp/model"
		save_new_model()
		test_new_model_saving()
