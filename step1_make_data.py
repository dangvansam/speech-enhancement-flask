from src.prepare_data import create_data

noise_id = 0
#-1 = all noise
# 0 = air_conditioner
# 1 = car_horn
# 2 = children_playing
# 3 = dog_bark
# 4 = drilling
# 5 = engine_idling
# 6 = gun_shot
# 7 = jackhammer
# 8 = siren
# 9 = street_music
voice_dir = '/media/trung/Data/vivos/data_train/'
# path_save_time_serie = '/media/trung/Data/log256/timeserie/'
# path_save_sound = '/media/trung/Data/log256/sound/'
# path_save_spectrogram = '/media/trung/Data/log256/spectrogram/'

path_save_spectrogram = '/media/trung/Data/log16k256_airconditioner/spectrogram/'
sample_rate = 8000*2
# Minimum duration of audio files to consider
min_duration = 1.0
#Frame length for training data
frame_length = 8063*2
# hop length for clean voice files
hop_length_frame = 8063*2
# hop length for noise files
hop_length_frame_noise = 5000*2
# How much frame to create for training
nb_samples = 10000
#nb of points for fft(for spectrogram computation)
n_fft = 255*2
#hop length for fft
hop_length_fft = 63

create_data(noise_id, voice_dir, path_save_spectrogram, sample_rate, min_duration, frame_length, hop_length_frame, hop_length_frame_noise, nb_samples, n_fft, hop_length_fft)