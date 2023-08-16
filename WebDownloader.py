import requests
import urllib.request
model_url=str(input("Enter Url"))
model_file=str(input("Enter File Name&Format:"))
d=requests.get(model_url,stream=True)
print ("Downloading...")
with open ("C:\\Users\\M\\Desktop\\test\\."+model_file,"wb")as f:
    for chunk  in d.iter_content(chunk_size=2400):
        f.write(chunk)
    f.close
    print("File Saved AS"+str(f))