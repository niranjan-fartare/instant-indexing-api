# Google Search Indexing Script

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

## Usage

1. Install required Python libraries:
   ```bash
   pip install oauth2client httplib2 pandas requests beautifulsoup4
2. Replace apidetails.json with your service account JSON key file.
3. Run the script:
   ```bash
   python indexing.py
2. Replace apidetails.json with your service account JSON key file.

## Configuration
1. Service Account Key: Replace apidetails.json with your service account JSON key file.
2. Sitemap: Modify the post-sitemap.xml variable to point to your desired sitemap.

## Customization

Adjust the time.sleep(2) duration for the delay between indexing requests based on your needs.
