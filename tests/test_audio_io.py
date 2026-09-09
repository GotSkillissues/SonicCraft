import os
import sys
import numpy as np

# Ensure the src directory is in the system path so we can import our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.audio_io import load_audio, save_audio, trim_audio, combine_audio, mix_audio

def run_tests():
    print("Starting audio_io tests...")
    sample_rate = 44100
    
    # 1. Generate a 1-second 440 Hz sine wave (Test Tone)
    t = np.linspace(0, 1, sample_rate, endpoint=False)
    test_tone = np.sin(2 * np.pi * 440 * t)
    
    # 2. Test Saving
    test_file = "test_tone.wav"
    save_audio(test_file, test_tone, sample_rate)
    print(f"Saved generated tone to {test_file}")
    
    # 3. Test Loading
    loaded_data, sr = load_audio(test_file)
    assert sr == sample_rate, "Sample rate mismatch!"
    print("Successfully loaded audio.")
    
    # 4. Test Trimming (Cut half a second)
    trimmed_data = trim_audio(loaded_data, 0, sample_rate // 2)
    save_audio("test_trimmed.wav", trimmed_data, sample_rate)
    print("Successfully trimmed audio (saved as test_trimmed.wav).")
    
    # 5. Test Combining (Glue two half-second clips together)
    combined_data = combine_audio(trimmed_data, trimmed_data)
    save_audio("test_combined.wav", combined_data, sample_rate)
    print("Successfully combined audio (saved as test_combined.wav).")
    
    # 6. Test Mixing (Mix a 440 Hz tone with an 880 Hz tone)
    tone_880 = np.sin(2 * np.pi * 880 * t)
    mixed_data = mix_audio(loaded_data, tone_880)
    save_audio("test_mixed.wav", mixed_data, sample_rate)
    print("Successfully mixed audio (saved as test_mixed.wav).")

    print("All tests passed! You can listen to the generated .wav files.")

if __name__ == "__main__":
    run_tests()