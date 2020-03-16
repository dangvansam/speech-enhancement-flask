from train_model import training

path_save_spectrogram = '/media/trung/Data/log/spectrogram/'
#path to find pre-trained weights / save models
weights_path = 'model/weights'
#pre trained model
name_model = 'model'
#Training from scratch vs training from pre-trained weights
training_from_scratch = True
#epochs for training
epochs = 80
#batch size for training
batch_size = 32

training(path_save_spectrogram, weights_path, name_model, training_from_scratch, epochs, batch_size)
