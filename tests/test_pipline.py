import unittest
import numpy as np
from deep_move.pipline import reshape_input


class TestPipline(unittest.TestCase):

	def test_reshape(self):
		img = np.zeros((5, 28, 28))
		resized_img = reshape_input(img)
		self.assertEqual(resized_img.shape, (5, 28 * 28))