import pickle
import pickle
import sklearn
from typing import Union
from sklearn.neural_network import MLPClassifier
from conf import config

SkLearnModel = Union[MLPClassifier]

def save_model(model: SkLearnModel):
	'''
		Save a SkLearn model in a file

		Parameters:
			model (SkLearnModel): SkLearn model of type (SkLearnModel)
	'''
	with open(config["model_path"], 'wb+') as file:
		pickle.dump(model, file)


def load_model() -> SkLearnModel:
	'''
		Load a SkLearn model

		Returns:
			SkLearn model of type (SkLearnModel)
	'''
	with open(config["model_path"], 'rb') as file:
		model = pickle.load(file)
	
	return model