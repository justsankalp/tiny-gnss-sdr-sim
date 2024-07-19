import numpy as np
from matplotlib import pyplot as plt

def sine(frequency, sample_rate, duration):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # Time axis
    sine_wave = np.sin(2 * np.pi * frequency * t)  # Sine wave
    return sine_wave

def compute_fft(signal, sample_rate):
    n = len(signal)
    freq = np.fft.fftfreq(n, d=1/sample_rate)
    fft_magnitude = np.fft.fft(signal)
    return freq, np.abs(fft_magnitude)

# Parameters
frequency = 50  # Frequency in Hertz
sample_rate = 1000  # Sample rate in samples per second
duration = 10  # Duration in seconds

# Generate sine wave
sine_wave = sine(frequency, sample_rate, duration)

# Compute FFT
frequencies, fft_magnitude = compute_fft(sine_wave, sample_rate)

# Plot the sine wave
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(sine_wave[:100])  # Plot the first 100 samples
plt.title("Sine Wave")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude")

# Plot the FFT
plt.subplot(2, 1, 2)
plt.plot(frequencies, fft_magnitude)
plt.title("FFT of the Sine Wave")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, sample_rate / 2)  # Plot only the positive frequencies

plt.tight_layout()
plt.show()
