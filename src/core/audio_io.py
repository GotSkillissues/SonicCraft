import numpy as np
import soundfile as sf

def load_audio(filepath):
    """Loads an audio file into a discrete-time NumPy array."""
    data, samplerate = sf.read(filepath)
    return data, samplerate

def save_audio(filepath, data, samplerate):
    """Saves a NumPy array back into an audio file."""
    sf.write(filepath, data, samplerate)

def trim_audio(data, start_sample, end_sample):
    """
    Cuts the audio. 
    In discrete-time terms, this is windowing a specific range of x[n].
    """
    return data[start_sample:end_sample]

def combine_audio(data1, data2):
    """
    Pastes/Appends audio.
    Concatenates two discrete-time signals together.
    """
    return np.concatenate((data1, data2))

def mix_audio(data1, data2):
    """
    Mixes two overlapping discrete-time signals.
    Handles arrays of different lengths and prevents audio clipping.
    """
    length1 = len(data1)
    length2 = len(data2)
    max_length = max(length1, length2)

    # Create an output array of zeros based on the maximum length.
    # This inherits the shape (e.g., mono or stereo channels) from data1.
    out_shape = list(data1.shape)
    out_shape[0] = max_length
    mixed = np.zeros(out_shape, dtype=data1.dtype)

    # Add the first signal into the empty array
    mixed[:length1] += data1
    
    # Add the second signal into the array
    mixed[:length2] += data2

    # Normalization: If adding the waves pushes the amplitude above 1.0 (clipping), 
    # we scale the entire array down so it sounds clean, not distorted.
    max_amp = np.max(np.abs(mixed))
    if max_amp > 1.0:
        mixed /= max_amp

    return mixed