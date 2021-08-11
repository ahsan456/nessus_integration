import requests
import json

base_url ="https://127.0.0.1:8834" 
url = base_url+"/scans"
querystring = {"folder_id":"3"}
payload = {"format": "csv"}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-ApiKeys": "accessKey=df1b6b0e82b16001a9d3b0117cde700b58e7aade578c5545403ce41a84202264;secretKey=85cdca00c18b99d30f8afe48105ee5abef587a2b4085e7b6a1c3479a8b8c6669"
}

response = requests.request("GET", url, headers=headers,verify=False)

# print(response.text)
# print(type())

data = json.loads(response.text)


scan_ids    = []
scan_export_id_token   = {}
for scan in data['scans']:
    scan_id = scan['id']
    scan_ids.append(scan_id)
    url = base_url+"/scans/5/export"
    response = requests.request("POST", url, json=payload, headers=headers,verify=False)

    scan_export_id_token[scan_id] =json.loads(response.text)

    # print(response.text)
    # print("***************************")



# status
export_scan_status = []
for key in scan_export_id_token:
    scan_id_token = scan_export_id_token[key] 
    url = base_url+"/scans/"+ str(key)+"/export/"+ str(scan_id_token['file'])+"/status"
    response = requests.request("GET", url, headers=headers,verify=False)
    export_scan_status.append(json.loads(response.text))

# print(scan_export_id_token)
print(export_scan_status)

    
# download
headers = {
    "Accept": "application/octet-stream",
    "X-ApiKeys": "accessKey=df1b6b0e82b16001a9d3b0117cde700b58e7aade578c5545403ce41a84202264;secretKey=85cdca00c18b99d30f8afe48105ee5abef587a2b4085e7b6a1c3479a8b8c6669"
}

# print()
scan_result = []
for key in scan_export_id_token:
    temp = []
    scan_id_token = scan_export_id_token[key] 
    url = base_url+"/scans/"+ str(key)+"/export/"+ str(scan_id_token['file'])+"/download"
    response = requests.request("GET", url, headers=headers,verify=False)
    
    temp.append(response.text)
    scan_result.append(temp)


    file_obj = open("scn_id_"+str(key)+"_report.csv","w")
    file_obj.write(response.text)
    file_obj.close()



print("files_wrote successfully")



# scan_result = []
# for key in scan_export_id_token:
#     temp = []
#     scan_id_token = scan_export_id_token[key] 
#     querystring = {"key":str(scan_id_token['token'])}

#     url = base_url+"/scans/"+ str(key)+"/attachments/"+ str(scan_id_token['file'])
#     response = requests.request("GET", url, headers=headers, params=querystring,verify=False)
#     temp.append(response.text)
#     scan_result.append(temp)


# print(scan_result)




# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print(scan_result)

    


# print(scan_ids)