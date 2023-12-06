from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

# https://developers.google.com/search/apis/indexing-api/v3/prereqs#header_2
JSON_KEY_FILE = "apidetails.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

def get_urls_from_sitemap(sitemap_url):
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.text, 'lxml')
    return [loc.text for loc in soup.find_all('loc')]

def indexURL(urls, http):
    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    LOG_FILE = "logs.txt"

    try:
        with open(LOG_FILE, 'r') as f:
            logged_urls = set(line.strip() for line in f)
    except FileNotFoundError:
        logged_urls = set()

    with open(LOG_FILE, 'a') as f:
        for u in urls:
            if u.strip() not in logged_urls:
                content = {
                    'url': u.strip(),
                    'type': "URL_UPDATED"
                }
                json_ctn = json.dumps(content)

                response, content = http.request(ENDPOINT, method="POST", body=json_ctn)
                result = json.loads(content.decode())

                if "error" in result:
                    print("Error({} - {}): {}".format(result["error"]["code"], result["error"]["status"], result["error"]["message"]))
                else:
                    print("urlNotificationMetadata.url: {}".format(result["urlNotificationMetadata"]["url"]))
                    print("urlNotificationMetadata.latestUpdate.url: {}".format(result["urlNotificationMetadata"]["latestUpdate"]["url"]))
                    print("urlNotificationMetadata.latestUpdate.type: {}".format(result["urlNotificationMetadata"]["latestUpdate"]["type"]))
                    print("urlNotificationMetadata.latestUpdate.notifyTime: {}".format(result["urlNotificationMetadata"]["latestUpdate"]["notifyTime"]))
                    
                    # Log the indexed URL
                    f.write(u.strip() + '\n')

                # Add a 2-second delay
                time.sleep(2)

# Sitemap URL
sitemap_url = "##"
urls_to_index = get_urls_from_sitemap(sitemap_url)

# Index URLs
indexURL(urls_to_index, http)
