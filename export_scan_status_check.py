import requests

url = "https://127.0.0.1:8834/scans/5/export/1426035555/status"

headers = {
    "Accept": "application/json",
    "X-ApiKeys": "accessKey=df1b6b0e82b16001a9d3b0117cde700b58e7aade578c5545403ce41a84202264;secretKey=85cdca00c18b99d30f8afe48105ee5abef587a2b4085e7b6a1c3479a8b8c6669"
}

response = requests.request("GET", url, headers=headers,verify=False)

print(response.text)
