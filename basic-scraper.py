import requests
import shutil

for x in range(1, 109):
    value = str(x)
    url = f"https://www.designyourway.net/drb/wp-content/uploads/2015/05/Beach-Wallpaper-Desktop-Background-{value}.jpg"
    fileName = f"{value}.jpg"

    r = requests.get(url, stream=True, headers={'User-agent': 'Mozilla/5.0'})
    if r.status_code == 200:
        with open(fileName, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)