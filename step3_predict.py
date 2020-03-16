from src.prediction_denoise import prediction

weights_path = 'model/weights'
#pre trained model
name_model = 'model'
#directory where read noisy sound to denoise
audio_dir_prediction = 'data/added_noise/'
#directory to save the denoise sound
dir_save_prediction = 'data/predict'
# Sample rate to read audio
sample_rate = 8000*2
# Minimum duration of audio files to consider
min_duration = 1.0
#Frame length for training data
frame_length = 8063*2
# hop length for sound files
hop_length_frame =8063*2
#nb of points for fft(for spectrogram computation)
n_fft = 255*2
#hop length for fft
hop_length_fft = 63

prediction(weights_path, name_model, audio_dir_prediction, dir_save_prediction, sample_rate, min_duration, frame_length, hop_length_frame, n_fft, hop_length_fft)
