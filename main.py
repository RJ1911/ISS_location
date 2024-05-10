import requests
import time

API_URL = "http://api.open-notify.org/iss-now.json"

def get_iss_location():
    try:
        response = requests.get(API_URL) # API call
        response.raise_for_status()
        data = response.json()
        return {
            "latitude": data["iss_position"]["latitude"],
            "longitude": data["iss_position"]["longitude"]
        }
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_iss_location(latitude, longitude):
    formatted_lat = f'Lat: {latitude:.4f}'
    formatted_long = f'Long: {longitude:.4f}'
    print(f"{formatted_lat} and {formatted_long}")

def main():
    while True:
        iss_data = get_iss_location()
        if iss_data:
            latitude = float(iss_data["latitude"])
            longitude = float(iss_data["longitude"])
            display_iss_location(latitude, longitude)
        time.sleep(5)  # Update every 5 seconds

if __name__ == "__main__":
    main()
