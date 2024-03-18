import requests

for i in range(1,20):
    url=f"https://networking-ecommerce-new.onrender.com/profile?id={i}"
    r=requests.get(url=url)
    print(r)
    print(i)
    if r.status_code==200:
        print(url)