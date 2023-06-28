
# # Import libraries
# import numpy as np
# from scipy import signal
# import scipy.fftpack
# from scipy.io.wavefile import read, write

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.popup import Popup
# from kivy.uix.filechooser import FileChooserListView


# class SoundFilterApp(App):
#     def build(self):
#         # Create a grid layout to hold the UI elements
#         layout = GridLayout(cols=2)

#         # Add a file chooser to select the input audio file
#         self.file_chooser = FileChooserListView()
#         layout.add_widget(self.file_chooser)

#         # Add a button to apply the filter
#         self.filter_button = Button(text='Apply Filter')
#         self.filter_button.bind(on_press=self.apply_filter)
#         layout.add_widget(self.filter_button)

#         # Add a text input field for the low cut-off frequency
#         self.lowcut_input = TextInput(text='500')
#         layout.add_widget(Label(text='Low cut-off frequency (Hz):'))
#         layout.add_widget(self.lowcut_input)

#         # Add a text input field for the high cut-off frequency
#         self.highcut_input = TextInput(text='2000')
#         layout.add_widget(Label(text='High cut-off frequency (Hz):'))
#         layout.add_widget(self.highcut_input)

#         # Add a text input field for the filter order
#         self.order_input = TextInput(text='5')
#         layout.add_widget(Label(text='Filter order:'))
#         layout.add_widget(self.order_input)

#         return layout

#     def apply_filter(self, instance):
#         # Get the selected input file and read the audio data
#         input_file = self.file_chooser.selection[0]
#         Fs, data = scipy.io.wavefile.read(input_file)

#         # Convert signal to frequency domain
#         fft_data = scipy.fftpack.fft(data)

#         # Get the filter parameters from the text input fields
#         lowcut = float(self.lowcut_input.text)
#         highcut = float(self.highcut_input.text)
#         order = int(self.order_input.text)

#         # Design band-pass filter
#         b, a = signal.butter(order, [lowcut, highcut], btype='band')

#         # Apply filter to signal
#         filtered_data = signal.fftconvolve(fft_data, b, mode='same')

#         # Convert filtered signal back to time domain
#         filtered_signal = scipy.fftpack.ifft(filtered_data)

#         # Normalize signal

#         filtered_signal /= np.max(np.abs(filtered_signal))

#         # Save filtered signal as a new audio file
#         output_file = input_file.replace('.wav', '_filtered.wav')
#         scipy.io.wavefile.write(output_file, Fs, filtered_signal)

#         # Display a popup to inform the user that the filtering is complete
#         popup = Popup(title='Filter Applied',
#                       content=Label(text='The filtered audio file has been saved to\n' + output_file),
#                       size_hint=(None, None), size=(400, 200))
#         popup.open()

# print('sayHi')

# from kivy.lang import Builder
# from kivymd.app import MDApp
# from kivymd.uix.screen import MDScreen

# class DribbleUI(MDScreen):
#     def __init__(self,**kw):
#         super().__init__(**kw)
    
# class App(MDApp):
#     def build(self):
#         return Builder.load_file('design.kv')
    

# if __name__ == '__main__':
#     App().run()



#----------------------------


# Import libraries
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

    # def apply_filter(self, instance):
    #     # Get the selected input file and read the audio data
    #     input_file = self.file_chooser.selection[0]
    #     Fs, data = read(input_file)

    #     # Convert signal to frequency domain
    #     fft_data = scipy.fftpack.fft(data)

    #     # Get the filter parameters from the text input fields
    #     lowcut = float(self.lowcut_input.text)
    #     highcut = float(self.highcut_input.text)
    #     order = int(self.order_input.text)

    #             # Design band-pass filter
    #     b, a = signal.butter(order, [lowcut, highcut], btype='band')

    #     # Apply filter to signal
    #     filtered_data = signal.fftconvolve(fft_data, b, mode='same')

    #     # Convert filtered signal back to time domain
    #     filtered_signal = scipy.fftpack.ifft(filtered_data)

    #     # Normalize signal
    #     filtered_signal /= np.max(np.abs(filtered_signal))

    #     # Save filtered signal as a new audio file
    #     output_file = input_file.replace('.wav', '_filtered.wav')
    #     write(output_file, Fs, filtered_signal)

    #     # Display a popup to inform the user that the filtering is complete
    #     popup = Popup(title='Filter Applied',
    #                   content=Label(text='The filtered audio file has been saved to\n' + output_file),
    #                   size_hint=(None, None), size=(400, 200))
    #     popup.open()

    #edited with lfilter instead of fftfilter

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
