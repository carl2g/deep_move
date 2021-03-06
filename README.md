# deep_move
The requirement for this project is only docker, to install docker on your laptop please follow the tutorial here https://docs.docker.com/get-docker/

## Train the model
To train the model, you can launch the script ./bin/train.sh

The last trained model will be automatically taken for prediction purpose.

## Using model
The images are assumed to be png format and of the size 28x28 ubytes
To use the model follows the steps:
- put your png image in the folder examples
- launch ./bin/predict.sh your_image_name.png

If successful you should have the result of the prediction in the file named prediction.json at the root of the repository.

## Testing
If you want to launch the test on your machine run ./bin/test.sh
