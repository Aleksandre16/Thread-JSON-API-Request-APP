import os
import requests
import json
import threading


#  DEF for requests !
def request_url(request_data_url, file_name):
    response = requests.get(request_data_url)
    if response.status_code == 200:
        data = response.json()
        with open(file_name, 'a') as file:
            json.dump(data, file)
            file.write("\n")
    else:
        print(f"Wrong API URL :  {request_data_url}")


folder_path = "json_files"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = os.path.join(folder_path, "all_products.json")

api_base_url = "https://dummyjson.com/products/"
api_urls = [f"{api_base_url}{i}" for i in range(1, 101)]  # გენერატორი 1-100-მდე ხელით რომ არ დაგვეწერა!


# MULTI THREADING! 
threads = []
for url in api_urls:
    thread = threading.Thread(target=request_url, args=(url, filename))
    threads.append(thread)
    thread.start()

# main thread-ი რომ დამთავრდეს სინქრონულად !
for thread in threads:
    thread.join()

print("successfully added ! ")
