import requests
from PIL import Image
from io import BytesIO


def load_image_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        image = Image.open(BytesIO(response.content))
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None



api_key = "Of33E2DkgriXEfxCX57f4bWmfZdrtIXywnmkeaUA"
giorno = "25-01-01"

parametri = {"api_key" :api_key, "date":giorno}

response = requests.get(
    url=f"https://api.nasa.gov/planetary/apod",params=parametri)

if response.ok:
    contenuto_risposta = response.json()
    load_image_from_url(contenuto_risposta["hdurl"]).show()
else:
    print("patatrak!")
    print(response.reason)