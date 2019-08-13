import requests 
  
url ="http://127.0.0.1:5000/uploader"
# data ="D:\coding\py\webpage\data\img.jpg"
files = {'file': open('data\img.jpg', 'rb')}
# data=""
# sending post request and saving response as response object 
r = requests.post(url = url, files=files) 
# r = requests.get(url = url) 
  
# extracting response text  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url)