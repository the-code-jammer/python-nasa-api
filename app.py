import requests

API_URL = "https://api.nasa.gov/planetary/apod?api_key=your_key_here"

def download_nasa_image():
    api_response = requests.get(API_URL)
    if api_response.status_code != 200:
        print(api_response.json())
        raise Exception(api_response.json())
    image_url = api_response.json().get("url")
    file_name = image_url.split("/")[-1]
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(img_response.content)

def main():
    download_nasa_image()
    
if __name__ == "__main__":
    main()