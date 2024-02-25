import requests

class GoogleMapsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/directions/json"

    def get_directions(self, origin, destination):
        params = {
            "origin": origin,
            "destination": destination,
            "key": self.api_key
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        if data["status"] == "OK":
            routes = data["routes"]
            for route in routes:
                steps = route["legs"][0]["steps"]
                for step in steps:
                    print(step["html_instructions"])
                    print("Distance:", step["distance"]["text"])
                    print("Duration:", step["duration"]["text"])
                    print("-------------------------")
        else:
            print("Error:", data["status"])

# Ejemplo de uso
if __name__ == "__main__":
    api_key = "AIzaSyC_nVTLeJe4a0EnO6xHmZ2Kikvu9R0sIag"
    maps_api = GoogleMapsAPI(api_key)
    origin = input("Introduce el punto de partida: ")
    destination = input("Introduce el punto de llegada: ")
    maps_api.get_directions(origin, destination)
