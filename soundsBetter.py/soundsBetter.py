
"""
test it extensivly
"""
import tkinter as tk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import librosa
from scipy.signal import spectrogram, istft
import soundfile as sf
import numpy as np

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.select_button = tk.Button(self)
        self.select_button["text"] = "Select WAV file"
        self.select_button["command"] = self.select_file
        self.select_button.grid(row=0, column=0)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().grid(row=1, column=0)

    def select_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
        if not filepath:
            return
        self.process_file(filepath)

    def process_file(self, filepath):
        # Load audio file
        data, rate = librosa.load(filepath, sr=None)

        # Create a spectrogram of the audio
        freqs, times, spec = spectrogram(data, fs=rate, nperseg=2048)

        # Select a section of audio where only noise is present
        noise_freqs, noise_times, noise_spec = spectrogram(data[10000:15000], fs=rate, nperseg=2048)

        # Estimate the noise power spectral density
        noise_psd = np.mean(noise_spec, axis=1)

        # Perform spectral subtraction
        reduction_factor = 0.3  # Reduce this value to decrease the amount of noise reduction
        clean_spec = spec - noise_psd[:, None]
        clean_spec = np.maximum(clean_spec, 0)

        # Convert back to time domain
        _, reduced_noise = istft(clean_spec, fs=rate)

        # Save the result
        sf.write("output_clean.wav", reduced_noise, rate)

        # Plot original and cleaned audio
        self.figure.clear()
        ax1 = self.figure.add_subplot(211)
        ax2 = self.figure.add_subplot(212)

        time = np.arange(len(data)) / rate
        ax1.plot(time, data)
        ax1.set_title("Original audio")

        time = np.arange(len(reduced_noise)) / rate
        ax2.plot(time, reduced_noise)
        ax2.set_title("Cleaned audio")

        self.canvas.draw()

root = tk.Tk()
app = Application(master=root)
app.mainloop()



#OLD ONE NOW IN GIT:

#Filter:

"""
# More functionality, more broken..
import numpy as np
from scipy import signal
import scipy.fftpack

import scipy.io 
from scipy.io import wavfile
from scipy.io.wavfile import read, write

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView


class SoundFilterApp(App):
    def build(self):
        # Create a grid layout to hold the UI elements
        layout = GridLayout(cols=2)

        # Add a file chooser to select the input audio file
        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)

        # Add a button to apply the filter
        self.filter_button = Button(text='Apply Filter')
        self.filter_button.bind(on_press=self.apply_filter)
        layout.add_widget(self.filter_button)

        # Add a text input field for the low cut-off frequency
        self.lowcut_input = TextInput(text='500')
        layout.add_widget(Label(text='Low cut-off frequency (Hz):'))
        layout.add_widget(self.lowcut_input)

        # Add a text input field for the high cut-off frequency
        self.highcut_input = TextInput(text='2000')
        layout.add_widget(Label(text='High cut-off frequency (Hz):'))
        layout.add_widget(self.highcut_input)

        # Add a text input field for the filter order
        self.order_input = TextInput(text='5')
        layout.add_widget(Label(text='Filter order:'))
        layout.add_widget(self.order_input)

        return layout

    def apply_filter(self, instance):
        # Get the selected input file and read the audio data
        input_file = self.file_chooser.selection[0]
        Fs, data = read(input_file)

        # Remove the DC component from the signal
        data = signal.detrend(data)

        # Get the filter parameters from the text input fields
        lowcut = float(self.lowcut_input.text)
        highcut = float(self.highcut_input.text)
        order = int(self.order_input.text)

        # Design band-pass filter
        b, a = signal.butter(order, [lowcut, highcut], btype='band')

        # Apply filter to signal
        filtered_signal = signal.lfilter(b, a, data)

        # Normalize signal
        #error here
        filtered_signal = signal.normalize(filtered_signal, scale=2, copy=False)

        # Extract the real part of the filtered signal
        filtered_signal = np.real(filtered_signal)

        # Save filtered signal as a new audio file
        output_file = input_file.replace('.wav', '_filtered.wav')
        write(output_file, Fs, filtered_signal)

        # Display a popup to inform the user that the filtering is complete
        popup = Popup(title='Filter Applied',
                  content=Label(text='The filtered audio file has been saved to\n' + output_file),
                  size_hint=(None, None), size=(400, 200))
        popup.open()


# Run the app
if __name__ == '__main__':
    SoundFilterApp().run()

"""
