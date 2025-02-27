import requests

headers = {"Content-Type" : "application/json", "X-Api-Key":"live_AdwgamLSst6l3PgUnm77diOJ7qzglHzsuWRKicbZ2VU1JLFsBvxY024DdOeE0q4m"}

get_cat = requests.get("https://api.thecatapi.com/v1/images/search")
print(get_cat.status_code)
print(get_cat.json())
cat = get_cat.json()[0]
cat_id = cat["id"]
print(cat_id)


data_vote = {f"image_id":f"{cat_id}","sub_id":"demo-0.55267371746242225","value":1}
data_favourite = {f"image_id":f"{cat_id}","sub_id":"demo-0.55267371746242225"}

vote_cat = requests.post("https://api.thecatapi.com/v1/votes/", headers = headers, json = data_vote)
print(vote_cat.json())
print(vote_cat.status_code)

get_favourite = requests.get("https://api.thecatapi.com/v1/favourites", headers = headers)
print(get_favourite.json())
print(get_favourite.status_code)

send_favourite = requests.post("https://api.thecatapi.com/v1/favourites", headers = headers, json = data_favourite)
print(send_favourite.status_code)
get_favourite_new = requests.get("https://api.thecatapi.com/v1/favourites", headers = headers)
print(get_favourite_new.json())

my_len = len(get_favourite_new.json())
my_cat = get_favourite_new.json()[my_len-1]
print(my_cat)

cat_id = my_cat["id"]
delete_cat = requests.delete(f"https://api.thecatapi.com/v1/favourites/{cat_id}", headers=headers)
print(delete_cat.status_code)