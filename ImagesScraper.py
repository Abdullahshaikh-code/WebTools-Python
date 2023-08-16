from ast import Str
from tkinter import END
from urllib import request
from urllib.error import HTTPError
import requests
from requests import Timeo

def url():
    url = str(input("Enter web Url "))
    return url


def data(web):
   try: 
     connection = request.urlopen(web, timeout=12,END,True) 
     html_code = connection.read()
     decoding = html_code.decode("utf8")
     return decoding
   except HTTPError as t:
    print (t)


def base_url_sclicing(web):
    # ---Base url---
    main_url = web
    b1 = main_url.find("/", 0)
    b2 = main_url.find("/", b1+2)
    if main_url.startswith("http"):
        base_url = main_url[b1-5:b2]
    if main_url.startswith("https"):
        base_url = main_url[b1-6:b2]
    return base_url


def image(decod, url_sclicing):
    count = -1
    img_tag = 100
    src_tag = -1
    while img_tag >= 0 or i2 >= 0:
        img_tag = decod.find("<img", count+1)
        if img_tag < 0:
            i1 = decod.find("src", src_tag+1)
            i2 = decod.find('"', i1)
            i3 = decod.find('"', i2+1)
            img_scd_url = decod[i2+1:i3]
            count = i1
            if count < 0:
                break
            if img_scd_url.startswith("https:"):
                image_url = img_scd_url
            else:
                image_url = url_sclicing+img_scd_url
            with requests.get(image_url, stream=True, timeout=12) as r:
                print("Downloading")
                with open("C:\\Users\\M\\Desktop\\test\\"+str(count)+"r1.jpg", "wb") as f:
                    for chunk in r.iter_content(chunk_size=2400):
                        f.write(chunk)
            f.close
            print("File saved as"+img_scd_url,)
        else:
            i1 = decod.find("src", img_tag)
            i2 = decod.find('"', i1)
            i3 = decod.find('"', i2+1)
            img_scd_url = decod[i2+1:i3]
            count = img_tag
            if count < 0:
                break
            if img_scd_url.startswith("https:"):
                image_url = img_scd_url
            else:
                image_url = url_sclicing+img_scd_url
            with requests.get(image_url, stream=True, timeout=12) as r:
                print("Downloading")
                with open("C:\\Users\\M\\Desktop\\test\\"+str(count)+"e1.jpg", "wb") as f:
                    for chunk in r.iter_content(chunk_size=10000):
                        f.write(chunk)
            f.close
            print("File saved"+str(f))
def one_image(web):
    image_one = web
    with requests.get(image_one, stream=True, timeout=12) as r:
        print("Downloading")
        with open(r"C:\\Users\\M\\Desktop\\test\\2km.jpg", "wb") as f:
            for chunk in r.iter_content(chunk_size=10000):
                f.write(chunk)
    f.close
    print("File saved"+image_one)
def print_menu():      
    print ("1. Whole page Images")
    print ("2.Single Image")
    print ("3. Exit")
    menu= int(input("Enter...."))
    if menu==1:
        web = url()
        decod = data(web)
        url_sclicing = base_url_sclicing(web)
        image(decod, url_sclicing)
        print_menu()
    if menu==2:
        web = url()
        one_image(web)
        print_menu()
    if menu==3: END

print_menu()
