import requests
req=requests.get("https://httpstatuses.com/")
document=req.content.decode("utf-8")
print(document)
f=open("index.html","w")
f.write(document)
f.close()