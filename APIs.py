import requests

def get_weather(city, api_key):
    # API endpoint for fetching weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert response data (JSON format) to a dictionary
        data = response.json()
        
        # Extract specific information from the data
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        
        # Print weather information
        print(f"Weather in {city.capitalize()}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Error: Unable to fetch weather data for {city}. Status code: {response.status_code}")

# Example usage
city = "London"
api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
get_weather(city, api_key)
