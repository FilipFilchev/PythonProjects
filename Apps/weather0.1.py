import tkinter as tk
import requests

API_KEY = 'YOUR_API_KEY'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] != '404':
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        result = f'Temperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'
        lbl_result.config(text=result)
    else:
        lbl_result.config(text='City not found.')

def search():
    city = entry_city.get()
    get_weather(city)

# Create the main window
window = tk.Tk()
window.title('Weather App')

# Create and configure the widgets
lbl_city = tk.Label(window, text='Enter City:')
lbl_city.pack()

entry_city = tk.Entry(window)
entry_city.pack()

btn_search = tk.Button(window, text='Search', command=search)
btn_search.pack()

lbl_result = tk.Label(window, text='')
lbl_result.pack()

# Run the main event loop
window.mainloop()
