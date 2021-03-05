import idx2numpy
import numpy as np
from .conf import config
from typing import Tuple
from imblearn.under_sampling import RandomUnderSampler


def get_dataset() -> Tuple[np.ndarray, np.ndarray]:
	'''
		Return a balanced mnist dataset 

		Returns: 
			A Tuple of (np.ndarray, np.ndarray) of dim (n, ...) representing the labels and features
	'''
	with open(config["train_labels"], 'rb') as file_labels:
		labels = idx2numpy.convert_from_file(file_labels)
	
	with open(config["train_images"], 'rb') as file_images:
		images = idx2numpy.convert_from_file(file_images)

	return labels, images
