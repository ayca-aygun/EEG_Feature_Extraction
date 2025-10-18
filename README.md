# EEG_Feature_Extraction
This repository includes Python code to pre-process the EEG channels with Kalman smoother and Independent Component Analysis, then to extract meaningful features.

# EEG ICA Blink Removal & ERP Calculation

This repository contains Python scripts to perform:
- ICA decomposition of EEG signals
- Automatic identification and removal of blink-related components
- ERP calculation and smoothing using Kalman filters
- Feature extraction for classification

## File Descriptions

- `calculate_ICA.py`: Applies ICA to EEG and visualizes components.
- `calculate_fm.py`: Extracts statistical and distance-based features from ICA components.
- `ERP_average_calculation.py`: Averages ERP across trials after blink removal.
- `eventTimes.py`: Extracts onset and response times from DRT markers.
- `README.md`: This file.

## How to Use

1. Make sure all dependencies (numpy, matplotlib, scikit-learn, etc.) are installed.
2. Prepare EEG data and DRT marker vectors.
3. Run `ERP_average_calculation.py` to perform blink-removal and ERP averaging.
4. Adjust hyperparameters as needed for your specific dataset.

## Requirements

- Python 3.6+
- numpy
- scipy
- scikit-learn
- matplotlib
