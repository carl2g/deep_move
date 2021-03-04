import idx2numpy
import numpy as np
from conf import config
from typing import Tuple
from imblearn.under_sampling import RandomUnderSampler


def get_dataset() -> Tuple[np.ndarray, np.ndarray]:
	'''
		Return a balanced mnist dataset 

		Returns: 
			A Tuple of (np.ndarray, np.ndarray) of dim (n, ...) representing the labels and features
	'''
	file_labels = open(config["train_labels"], 'rb')
	file_images = open(config["train_images"], 'rb')
	return idx2numpy.convert_from_file(file_labels), idx2numpy.convert_from_file(file_images)
