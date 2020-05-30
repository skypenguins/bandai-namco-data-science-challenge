import librosa
import numpy as np
from pathlib import Path

raw_dir_path = Path('./dist-data/noised_tgt/')
output_dir_path = './output_wav/noised_tgt/'

raw_files_list = list(raw_dir_path.glob('*.npy'))
num_of_files = len(list(raw_dir_path.glob('*.npy')))
for filepath in raw_files_list:
    print('{}をwavファイルに変換中...{}/{}'.format(filepath.name, raw_files_list.index(filepath) + 1, num_of_files))
    sr = 22050

    mel = np.load(filepath)
    y = librosa.feature.inverse.mel_to_audio(mel)

    print(y.shape)

    librosa.output.write_wav(output_dir_path + filepath.stem + '.wav', y, sr)

