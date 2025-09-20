import requests
import json

url = "https://scholars.cmu.edu/api/users"

payload = json.dumps({
  "params": {
    "by": "text",
    "category": "user",
    "text": ""
  },
  "filters": [
    {
      "name": "department",
      "matchDocsWithMissingValues": True,
      "useValuesToFilter": False
    },
    {
      "name": "customFilterThree",
      "matchDocsWithMissingValues": True,
      "useValuesToFilter": False
    },
    {
      "name": "tags",
      "matchDocsWithMissingValues": True,
      "useValuesToFilter": False
    },
    {
      "name": "customFilterOne",
      "matchDocsWithMissingValues": True,
      "useValuesToFilter": False
    },
    {
      "name": "customFilterTwo",
      "matchDocsWithMissingValues": True,
      "useValuesToFilter": False
    }
  ]
})
headers = {
  'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
  'Connection': 'keep-alive',
  'Origin': 'https://scholars.cmu.edu',
  'Referer': 'https://scholars.cmu.edu/search?by=text&type=user&v=computer',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
  'accept': 'application/json',
  'content-type': 'application/json',
  'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'Cookie': 'cookieConsent=WzAsZmFsc2Vd'
}

response = requests.request("POST", url, headers=headers, data=payload)
with open("test.txt", "w") as file:
    file.write(response.text)

#print(response.text)
