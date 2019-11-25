from keras.applications import VGG16
from keras.models import model_from_json
from keras_applications import imagenet_utils




json_file = open('transfer_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("transfermodel.h5")
print("Loaded model from disk")
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

model = VGG16(weights="imagenet", include_top=False)
model.summary()


def create_features(dataset, pre_model):
    x_scratch = []
    i = 0
    # loop over the images
    print("loop started")
    for imagePath in dataset:
        print("image", i, "\n")
        # load the input image and image is resized to 224x224 pixels
        # 299x299 for inceptionV3
        image = load_img(imagePath, target_size=(224, 224))
        image = img_to_array(image)

        # preprocess the image by (1) expanding the dimensions and
        # (2) subtracting the mean RGB pixel intensity from the
        # ImageNet dataset
        image = np.expand_dims(image, axis=0)
        image = imagenet_utils.preprocess_input(image)

        # add the image to the batch
        x_scratch.append(image)
        i += 1
    print("for loop done")

    x = np.vstack(x_scratch)
    features = pre_model.predict(x, batch_size=32)
    # features_flatten = features.reshape((features.shape[0], 7 * 7 * 512))
    return x, features


train_x, test_features = create_features(["static/images/DR1.jpg"], model)
preds = np.argmax(loaded_model.predict(test_features[:472]), axis=1)