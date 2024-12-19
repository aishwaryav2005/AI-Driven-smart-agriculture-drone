import requests

def send_image_to_ai(image_path):
    api_url = "https://chatgpt.com/g/g-6PKrcgTBL-planty/c/66ffc8d1-1388-8013-aa80-e39ebae32359"
    with open(image_path, 'rb') as image_file:
        files = {'file': image_file}
        response = requests.post(api_url, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to get analysis. Status code: {response.status_code}"}
