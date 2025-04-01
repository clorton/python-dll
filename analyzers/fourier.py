import numpy as np

class Frequency():
    def __init__(self):
        return

    def analyze(self, model):

        y = model.output
        Y = np.fft.fft(y)                      # Perform FFT
        freqs = np.fft.fftfreq(len(y), d=model.dx)   # Frequency bins

        # Only take the positive half
        half = len(y) // 2
        mag = np.abs(Y[:half])
        positive_freqs = freqs[:half]

        # Find the index of the peak
        peak_idx = np.argmax(mag)
        dominant_freq = positive_freqs[peak_idx]

        print(f"Dominant frequency: {dominant_freq} cycles/unit")
