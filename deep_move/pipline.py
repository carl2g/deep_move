import numpy as np
from imblearn.pipeline import Pipeline
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.neural_network import MLPClassifier


def reshape_input(x: np.ndarray):
	return np.reshape(x, (x.shape[0], 28 * 28))


def get_pipline():
	return Pipeline([
		('reshape', FunctionTransformer(reshape_input)),
		('sampler', RandomUnderSampler(random_state=0)),
		('standerdize', StandardScaler()),
		('classifier', MLPClassifier(verbose=10))
	])