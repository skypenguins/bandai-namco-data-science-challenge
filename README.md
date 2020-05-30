# My participation log of the Bandai Namco Data Science Challenge competition
This repo contains my solution to the Bandai Namco Data Science Challenge competition.

## Overview
The objective of this competition was to remove the artificial noise from the given voice data.
The voice data was converted into Mel Spectrogram.

### Dataset
  - raw\[0-9\]\{3\}.npy - Mel Spectrogram of raw voice data
    - 100 files
  - noised_tgt_\[0-9\]\{3\}.npy - Mel Spectrogram of noised voice data
    - 30 files

## My solution
I used a pix2pix model to achieve this competition.

## Prerequisites
  - [become-yukarin](https://github.com/Hiroshiba/become-yukarin)
## License
[MIT License](./LICENSE)
