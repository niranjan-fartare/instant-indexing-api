# Google Search Indexing Python Script

## Overview

This Python script simplifies the process of submitting URLs for indexing to the Google Search Indexing API. It is particularly useful when dealing with a large number of URLs, such as those present in an XML sitemap. The script utilizes a service account for authentication and incorporates a delay between indexing requests to comply with API usage guidelines.

## Features

- **Authentication**: Utilizes the Google Search Indexing API with OAuth 2.0 authentication using a service account.
  
- **Sitemap Parsing**: Extracts URLs from a specified XML sitemap using BeautifulSoup.

- **Indexing**: Submits URLs to the Google Search Indexing API for inclusion in Google's search index.

- **Logging**: Logs indexed URLs to a `logs.txt` file to prevent duplicate indexing.

- **Delay Mechanism**: Incorporates a configurable delay of 2 seconds between indexing requests to avoid rate limits.

## Prerequisites

- Python 3
- Service account JSON key file (`apidetails.json`) with necessary permissions for the Google Search Indexing API.

## How to obtain Authentication Credentials?

**Enable Google Search Indexing API:**
- Go to the Google Cloud Console.
- Create a new project or select an existing one.
- Navigate to the "APIs & Services" > "Library" section.
- Search for "Google Search Indexing API" and enable it for your project.

**Create a Service Account:**
- In the Google Cloud Console, navigate to "IAM & Admin" > "Service accounts."
- Click on "Create Service Account" at the top.
- Enter a name for your service account, e.g., "indexing-service-account."
- Assign the role "Owner" to the service account (for simplicity; adjust permissions based on your needs).
- Click on "Create" to create the service account.

**Generate and Download JSON Key File:**
- After creating the service account, click on the service account name in the Service accounts list.
- Go to the "Keys" tab.
- Click on "Add Key" > "Create new key."
- Choose JSON as the key type and click "Create." This will download a JSON key file (cred.json) to your computer.

**Add Service Account to Search Console:**
- Visit Google Search Console.
- Select your website property or add your website and verify ownership if not done already.
- In the Search Console, navigate to "Settings" > "Users and permissions."
- Click on "Add User" and enter the email address of the service account created earlier.
- Assign "Owner" permissions to the service account.
- Click "Add" to grant access.

## Usage

1. Clone or download this script & naviagate to the folder.
2. Install required Python libraries:
   ```bash
   pip install oauth2client httplib2 pandas requests beautifulsoup4
3. Replace apidetails.json with your service account JSON key file.
4. Run the script:
   ```bash
   python indexing.py
5. Replace "##" with an actual xml sitemap url on line 58.

## Configuration
1. Service Account Key: Replace apidetails.json with your service account JSON key file or you can copy paste the details from your json file to the apidetails.json file.
2. Sitemap: Modify the post-sitemap.xml variable to point to your desired sitemap on line 58.
3. Adjust the time.sleep(2) duration for the delay between indexing requests based on your needs.
