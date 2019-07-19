import requests

serverhostname = "YOUR_SONARR_HOSTNAME"
apikey = "YOUR_SONARR_API_KEY_GOES_HERE"
mediafolder = "/media/downloads_completed/"
response = requests.get(
    "http://"+serverhostname+":8989/api/manualimport?folder="+mediafolder+"&sort_by=qualityWeight&order=desc",
    headers={"X-Api-Key": apikey},
)

files = []

for x in response.json():
    print(x["path"])
    newfile={"path":x["path"], "folderName":x["folderName"], "seriesId":x["series"]["id"]}
    episodeids = []
    for episodes in x["episodes"]:
        episodeids.append(episodes["id"])
    newfile["episodeIds"] = episodeids
    newfile["quality"] = x["quality"]
    files.append(newfile)
 
print(files) 
response = requests.post("http://"+serverhostname+":8989/api/command", json={"name":"manualImport","files":files,"importMode":"Move"}, headers={"X-Api-Key": apikey})

print(response.json())