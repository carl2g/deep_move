import unittest
from deep_move.dataset import get_dataset


class TestDataset(unittest.TestCase):

	def test_feature_shape(self):
		_, features =  get_dataset()
		self.assertEqual(features.shape[1:], (28, 28))
	
	def test_label_shape(self):
		labels, features =  get_dataset()
		self.assertEqual(features.shape[0], labels.shape[0])
