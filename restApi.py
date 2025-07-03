import requests
ch=input("Enter the word : ")
# url=f"https://api.datamuse.com/words?ml={ch}"
# response=requests.get(url)
# data=response.json()

# if response.status_code==200:
#     for item in data:
#         print(item["tag"][0])


url=f"https://api.datamuse.com/words?rel_jjb={ch}"
response=requests.get(url)
data=response.json()

if response.status_code==200:
    for item in data:
        if item.get('score') > 950 :
            print(item.get('word'))