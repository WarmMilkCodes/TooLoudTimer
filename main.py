import tkinter as tk
import pyaudio
import numpy as np
import threading
import time

# Parameters
AUDIO_THRESHOLD = 0.1  # Adjust this value based on noise level
RATE = 44100
CHUNK = 1024
NUM_BARS = 50  # Number of frequency bands to display

class AudioTimerApp:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.start_time = 0
        self.total_elapsed_time = 0
        
        # Create GUI
        self.timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)
        
        self.canvas = tk.Canvas(root, width=600, height=200, bg="black")
        self.canvas.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Listening", command=self.start_listening)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(root, text="Stop Listening", command=self.stop_listening, state="disabled")
        self.stop_button.pack(pady=10)

        # Audio Stream
        self.audio_stream = pyaudio.PyAudio().open(format=pyaudio.paFloat32,
                                                   channels=1,
                                                   rate=RATE,
                                                   input=True,
                                                   frames_per_buffer=CHUNK)
    
    def start_listening(self):
        self.running = True
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        threading.Thread(target=self.listen_for_audio).start()

    def stop_listening(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def listen_for_audio(self):
        while self.running:
            audio_data = np.frombuffer(self.audio_stream.read(CHUNK, exception_on_overflow=False), dtype=np.float32)
            volume = np.linalg.norm(audio_data)
            if volume > AUDIO_THRESHOLD:
                if self.start_time == 0:
                    self.start_time = time.time()
                self.update_timer()
            else:
                if self.start_time > 0:
                    # Add the current session's elapsed time to total elapsed time
                    self.total_elapsed_time += time.time() - self.start_time
                    self.start_time = 0
                self.update_timer(reset=False)
            # Visualize the frequency spectrum
            self.visualize_frequency(audio_data)

    def update_timer(self, reset=False):
        if reset:
            self.timer_label.config(text="00:00:00")
        else:
            current_elapsed_time = 0
            if self.start_time > 0:
                current_elapsed_time = time.time() - self.start_time
            total_time = self.total_elapsed_time + current_elapsed_time
            minutes, seconds = divmod(int(total_time), 60)
            hours, minutes = divmod(minutes, 60)
            self.timer_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    def visualize_frequency(self, data):
        self.canvas.delete("all")  # Clear the canvas
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Compute FFT and frequency spectrum
        fft = np.fft.rfft(data)
        fft_magnitude = np.abs(fft)
        
        # Normalize magnitude for visualization
        fft_magnitude = fft_magnitude[:NUM_BARS]  # Limit to NUM_BARS bands
        fft_magnitude = fft_magnitude / np.max(fft_magnitude) if np.max(fft_magnitude) > 0 else fft_magnitude
        fft_magnitude *= height  # Scale to canvas height

        bar_width = width // NUM_BARS
        for i in range(NUM_BARS):
            x0 = i * bar_width
            x1 = x0 + bar_width - 2  # Add spacing between bars
            y0 = height
            y1 = height - fft_magnitude[i]
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="green")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Too Loud Timer")
    app = AudioTimerApp(root)
    root.mainloop()
