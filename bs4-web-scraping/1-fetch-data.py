import requests

def fetchAndSaveToFile(url,path):
    r = requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/videos/international/houthis-attack-second-us-drone-in-3-days-mq-9-reaper-hit-angry-trump-bombs-sanaa/videoshow/119968757.cms"

fetchAndSaveToFile(url,"data/times.html")