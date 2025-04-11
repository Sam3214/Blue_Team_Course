#Project
import requests
def get_IOCs(url):
    try:
      api = "https://api.iocparser.com/url"
      payload = {"url": url}
      headers = {'Content-Type': 'application/json',}
      response = requests.request("POST", api, headers=headers, json = payload)
      results=response.json()
      if results["status"]=="success":
        print("MD5 hashes")
        md5_hash=results["data"]["FILE_HASH_MD5"]
        print(md5_hash)
        print()
        print("SHA256 hashes")
        sha256_hash=results["data"]["FILE_HASH_SHA256"]
        print(sha256_hash)
        print()
        print("SHA1 hashes")
        sha1_hash=results["data"]["FILE_HASH_SHA1"]
        print(sha256_hash)
        print()
        print("URLs")
        malicious_url=results["data"]["URL"]
        print(malicious_url)
        print()
    except:
      pass    

url=input("Enter the website link :")

get_IOCs(url)
