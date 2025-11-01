from urllib.parse import quote
import requests
import json

url = "https://scholars.cmu.edu/api/users"
groupUrl = "https://scholars.cmu.edu/api/groups"
groupIdToCollege = {}
existingGroups = {"School of Computer Science", "College of Engineering", "College of Fine Arts", "Dietrich College of Humanities and Social Sciences", "Mellon College of Science", "Heinz College of Information Systems and Public Policy", "Tepper School of Business", "Carnegie Mellon University Qatar"}

try:
  payload = json.dumps({
    "params": {
      "by": "text",
      "category": "group"
    },
    "filters": []
  })
  headers = {
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://scholars.cmu.edu',
    'Referer': 'https://scholars.cmu.edu/search?by=text&type=group',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/json',
    'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'Cookie': 'cookieConsent=WzAsZmFsc2Vd; intercom-device-id-g60t55rg=277da096-9a12-4ab3-8c45-5b43203b4e63; intercom-session-g60t55rg=cythaWhXU2gyckxWdlpGT0NjeGxxTFl5a3MwV2wzWlBRU2lSeHpjRWNvRk5SbTlvYUpFRUN0T1FxY0ZTdWptUTN6OFh0cGpTckhGUGJTSXM5Qk9zcUZSZ1RpUXRSWUxNUFFoM0RzZm1idEU9LS1RajRwTTdlWGlxWWFvekhvZUpoeHhBPT0=--d8895826a2542ca0682d630fa2470e0a9bf3f9f5'
  }

  response = requests.request("POST", groupUrl, headers=headers, data=payload)
  resource_dict = response.json()["resource"]
  for resource in resource_dict:
    name = resource["name"]
    if name == "Software Engineering Institute":
      name = "School of Computer Science"
    elif name not in existingGroups:
      name = "UnAffliated"
    groupIdToCollege[resource["discoveryId"]] = name
except Exception as e:
    print(f"Error: {e}")

print(f'Group Ids Mapping: {groupIdToCollege}')

i=0
while i <= 600:
  try:
    payload = json.dumps({
      "params": {
        "by": "text",
        "category": "user",
        "text": ""
      },
      "pagination": {
        "startFrom": i,
        "perPage": 25
      },
      "sort": "lastNameAsc",
      "filters": [
        {
          "name": "customFilterOne",
          "matchDocsWithMissingValues": True,
          "useValuesToFilter": False
        },
        {
          "name": "tags",
          "matchDocsWithMissingValues": True,
          "useValuesToFilter": False
        },
        {
          "name": "customFilterTwo",
          "matchDocsWithMissingValues": True,
          "useValuesToFilter": False
        },
        {
          "name": "customFilterThree",
          "matchDocsWithMissingValues": True,
          "useValuesToFilter": False
        },
        {
          "name": "department",
          "matchDocsWithMissingValues": True,
          "useValuesToFilter": False
        }
      ]
    })
    headers = {
      'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
      'Connection': 'keep-alive',
      'Origin': 'https://scholars.cmu.edu',
      'Referer': 'https://scholars.cmu.edu/search?back&by=text&type=user&v=',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
      'accept': 'application/json',
      'content-type': 'application/json',
      'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"macOS"',
      'Cookie': '_fbp=fb.1.1737912968059.687169973194182488; intercom-device-id-g60t55rg=99a8b322-ca9c-4e53-a684-511bc7c79bd2; nmstat=9b9fe27a-7a1d-ae5c-5413-f4896c3de34a; _ga_CSELMMLRMD=GS1.1.1741908764.1.1.1741908793.0.0.0; _ga_KNY2R3YGW4=GS1.1.1742676420.2.0.1742676420.0.0.0; _ga_HLS6CLDDJ0=GS1.1.1742676420.2.0.1742676420.0.0.0; _ga_98MDFNBLD8=GS1.1.1744736574.2.0.1744736587.0.0.0; _ga_13JJ3J4BFN=GS2.1.s1747001828$o1$g1$t1747002026$j39$l0$h362112686; _ga_YR51ED8F5M=GS2.1.s1747064067$o2$g0$t1747064067$j0$l0$h0; _ga_6BQ1DR180Y=GS2.1.s1750213144$o1$g0$t1750213151$j53$l0$h0; _ga_SFHG83CLCK=GS2.2.s1751653646$o4$g0$t1751653646$j60$l0$h0; _ga_MJ4PLCDBT1=GS2.1.s1751658667$o1$g1$t1751659322$j60$l0$h0; _ga_159WZ6DDLJ=GS2.1.s1752353409$o1$g1$t1752353420$j49$l0$h0; _ga_V7S2SH5H31=GS2.1.s1752471073$o3$g1$t1752472260$j60$l0$h0; _ga_8L62C9XSY9=GS2.1.s1752614883$o7$g0$t1752614883$j60$l0$h0; _ga_6GN9LLBKF8=GS2.1.s1753824101$o7$g1$t1753825162$j60$l0$h0; _ga_6VFQE788X7=GS2.1.s1753824101$o6$g1$t1753825162$j60$l0$h0; _ga_PJEC7ZVERY=GS2.1.s1754334768$o9$g0$t1754334768$j60$l0$h0; _ga_RBQMFJGGR9=GS2.1.s1754426024$o1$g1$t1754426163$j60$l0$h0; _gcl_au=1.1.1482944350.1755487625; cf_clearance=LtNIk_qIpbwG_E3rD7.UyRjG4gFpEbcqYGXN1AQ08EI-1755551652-1.2.1.1-eblTSd.BKrN.LQW5FReSogocwRG97QyNCCYVEkAl8NxsPbE0frNLRRsPlT.2SFK43YNCrFozG2XOINVL4Yf2bY0AV61kVfiOgNnjlOvuvtRK2T86dOk_LJW8mo4_LXNixzrqOqLYqEsXN6L97WYz9TuxjB8eF9n97V3YIka3S.hcB6zT44WZFWGRe2jCnpMWr4qhv7PJcjExQ9.mOuxIRo1uxhdTKpImXLmN.epqpgo; _ga_DE8E2HJLQR=GS2.1.s1755551652$o2$g0$t1755551655$j57$l0$h0; _ga_9KH7F8345N=GS2.1.s1755551652$o2$g0$t1755551655$j57$l0$h0; _ga_WF4PSG218T=GS2.1.s1755551652$o2$g0$t1755551655$j57$l0$h0; _ga_4EXR1GJJ46=GS2.1.s1757013338$o100$g1$t1757013528$j38$l0$h0; _ga_ECPW5BRBQ7=GS2.2.s1757077164$o1$g1$t1757077168$j56$l0$h0; _ga_NRCLJZKD8M=GS2.1.s1757190938$o22$g0$t1757190939$j59$l0$h0; _ga_PWD1B5KLT7=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h0; _ga_ZRDQX035W5=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h0; _ga_1Y35V9RLL1=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h627040146; _ga_0LJ42RV7RF=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h0; _ga_R0F0JXXBNT=GS2.1.s1757190938$o16$g0$t1757190939$j59$l0$h0; _ga_9FZLDFJ28W=GS2.1.s1757190966$o1$g1$t1757192475$j60$l0$h0; _ga_P112DV9K94=GS2.1.s1757991103$o23$g0$t1757991103$j60$l0$h0; _ga_1XQYSMEBVE=GS2.1.s1757991103$o55$g0$t1757991103$j60$l0$h0; _ga_RD878ZQYTS=GS2.1.s1758322062$o15$g1$t1758322250$j60$l0$h0; cookieConsent=WzAsdHJ1ZV0=; _ga_NDRL038Y6K=GS2.1.s1758914625$o18$g0$t1758914626$j59$l0$h0; _gid=GA1.2.665515921.1759608703; _ga=GA1.1.14942026.1737912968; _ga_ZR1RG7B6F9=GS2.1.s1759608702$o1$g0$t1759608706$j56$l0$h0'
    }
    response_users = requests.request("POST", url, headers=headers, data=payload)
    data_dict = response_users.json()
    for j in data_dict["resource"]:
      iD = j["discoveryId"]
      firstName = j["firstName"]
      lastName = j["lastName"]
      
      prof_url = f"https://scholars.cmu.edu/api/users/{iD}"

      headers = {
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'keep-alive',
        'Referer': f'https://scholars.cmu.edu/{iD}-{quote(firstName)}-{quote(lastName)}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'content-type': 'application/json',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Cookie': '_fbp=fb.1.1737912968059.687169973194182488; intercom-device-id-g60t55rg=99a8b322-ca9c-4e53-a684-511bc7c79bd2; nmstat=9b9fe27a-7a1d-ae5c-5413-f4896c3de34a; _ga_CSELMMLRMD=GS1.1.1741908764.1.1.1741908793.0.0.0; _ga_KNY2R3YGW4=GS1.1.1742676420.2.0.1742676420.0.0.0; _ga_HLS6CLDDJ0=GS1.1.1742676420.2.0.1742676420.0.0.0; _ga_98MDFNBLD8=GS1.1.1744736574.2.0.1744736587.0.0.0; _ga_13JJ3J4BFN=GS2.1.s1747001828$o1$g1$t1747002026$j39$l0$h362112686; _ga_YR51ED8F5M=GS2.1.s1747064067$o2$g0$t1747064067$j0$l0$h0; _ga_6BQ1DR180Y=GS2.1.s1750213144$o1$g0$t1750213151$j53$l0$h0; _ga_SFHG83CLCK=GS2.2.s1751653646$o4$g0$t1751653646$j60$l0$h0; _ga_MJ4PLCDBT1=GS2.1.s1751658667$o1$g1$t1751659322$j60$l0$h0; _ga_159WZ6DDLJ=GS2.1.s1752353409$o1$g1$t1752353420$j49$l0$h0; _ga_V7S2SH5H31=GS2.1.s1752471073$o3$g1$t1752472260$j60$l0$h0; _ga_8L62C9XSY9=GS2.1.s1752614883$o7$g0$t1752614883$j60$l0$h0; _ga_6GN9LLBKF8=GS2.1.s1753824101$o7$g1$t1753825162$j60$l0$h0; _ga_6VFQE788X7=GS2.1.s1753824101$o6$g1$t1753825162$j60$l0$h0; _ga_PJEC7ZVERY=GS2.1.s1754334768$o9$g0$t1754334768$j60$l0$h0; _ga_RBQMFJGGR9=GS2.1.s1754426024$o1$g1$t1754426163$j60$l0$h0; _gcl_au=1.1.1482944350.1755487625; cf_clearance=LtNIk_qIpbwG_E3rD7.UyRjG4gFpEbcqYGXN1AQ08EI-1755551652-1.2.1.1-eblTSd.BKrN.LQW5FReSogocwRG97QyNCCYVEkAl8NxsPbE0frNLRRsPlT.2SFK43YNCrFozG2XOINVL4Yf2bY0AV61kVfiOgNnjlOvuvtRK2T86dOk_LJW8mo4_LXNixzrqOqLYqEsXN6L97WYz9TuxjB8eF9n97V3YIka3S.hcB6zT44WZFWGRe2jCnpMWr4qhv7PJcjExQ9.mOuxIRo1uxhdTKpImXLmN.epqpgo; _ga_DE8E2HJLQR=GS2.1.s1755551652$o2$g0$t1755551655$j57$l0$h0; _ga_9KH7F8345N=GS2.1.s1755551652$o2$g0$t1755551655$j57$l0$h0; _ga_WF4PSG218T=GS2.1.s1755551652$o2$g0$t1755551655$j57$l0$h0; _ga_4EXR1GJJ46=GS2.1.s1757013338$o100$g1$t1757013528$j38$l0$h0; _ga_ECPW5BRBQ7=GS2.2.s1757077164$o1$g1$t1757077168$j56$l0$h0; _ga_NRCLJZKD8M=GS2.1.s1757190938$o22$g0$t1757190939$j59$l0$h0; _ga_PWD1B5KLT7=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h0; _ga_ZRDQX035W5=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h0; _ga_1Y35V9RLL1=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h627040146; _ga_0LJ42RV7RF=GS2.1.s1757190938$o21$g0$t1757190939$j59$l0$h0; _ga_R0F0JXXBNT=GS2.1.s1757190938$o16$g0$t1757190939$j59$l0$h0; _ga_9FZLDFJ28W=GS2.1.s1757190966$o1$g1$t1757192475$j60$l0$h0; _ga_P112DV9K94=GS2.1.s1757991103$o23$g0$t1757991103$j60$l0$h0; _ga_1XQYSMEBVE=GS2.1.s1757991103$o55$g0$t1757991103$j60$l0$h0; _ga=GA1.1.14942026.1737912968; _ga_RD878ZQYTS=GS2.1.s1758322062$o15$g1$t1758322250$j60$l0$h0; cookieConsent=WzAsdHJ1ZV0=; _ga_NDRL038Y6K=GS2.1.s1758914625$o18$g0$t1758914626$j59$l0$h0'
      }

      response = requests.request("GET", prof_url, headers=headers)
      prof_data = response.json()
      print(f"Name: {firstName + ' ' + lastName}; Department: {prof_data["positions"][0]["department"]}; Email: {prof_data["emailAddress"]["address"]}")
    i += 25
  except Exception as e:
    print(f"Error: {e}")