import sklearn
from sklearn.model_selection import train_test_split
from dataset import get_dataset
from model import save_model
from pipline import get_pipline

if __name__ == "__main__":
	
	labels, features = get_dataset()

	pipe = get_pipline()

	pipe.fit(features, labels)

	save_model(pipe)