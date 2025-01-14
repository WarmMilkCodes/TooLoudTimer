# Too Loud Timer

**Too Loud Timer** is an interactive application that combines real-time audio monitoring with a timer to track noisy periods. Designed for teachers, students, or anyone managing a quiet environment, it starts a timer when noise exceeds a threshold and pauses when the environment becomes quiet. A dynamic frequency visualization adds a visual representation of the noise levels.

---

## Features

- **Audio-Activated Timer**:
  - Starts when noise exceeds a set threshold.
  - Pauses when the noise level drops below the threshold.
  - Tracks cumulative noisy time, even across multiple starts and stops.

- **Real-Time Frequency Visualization**:
  - Displays a bar graph of the sound frequencies for a more intuitive understanding of noise activity.

- **Simple and Customizable**:
  - Adjustable noise threshold for different environments.
  - Clean and user-friendly graphical interface.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/WarmMilkCodes/tooloudtimer.git
   cd too-loud-timer

2. Install dependencies:
   ```bash
   pip install pyaudio numpy
3. Run the application:
   ```bash
   python too_loud_timer.py

---

## Usage
1. Launch the application.
2. Click **Start Listening** to begin monitoring ambient noise.
3. The timer will start when noise exceeds the threshold and pause when it drops below.
4. Observe the real-time frequency visualization for feedback on noise levels.
5. Click **Stop Listening** to pause the app and review the total noisy time.

---

## Configuration
- **Noise Threshold**: Adjust the ```AUDIO_THRESHOLD``` parameter in the script to calibrate the sensitivity for different environments.
- **Frequency Bands**: Modify the ```NUM_BARS``` parameter to change the number of frequency bands displayed in the visualization.

---
## Requirements
- Python 3.x
- Libraries: ```pyaudio```, ```numpy```, ```tkinter```

---

## License
This project is licensed under the MIT License.

---
## Contributions
Contributions are welcome! Please feel free to submit issues or pull requests.

---
## Acknowledgments
- Built with ```pyaudio``` for audio input and ```tkinter``` for the graphical interface.
- Inspired by the need for effective noise management in classrooms and workspaces.
