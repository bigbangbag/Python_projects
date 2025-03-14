import requests
from bs4 import BeautifulSoup

url = "https://github.com"  # Replace with the desired website

# Send a GET request to fetch the webpage content
response = requests.get(url)

if response.status_code == 200:
    # Parse the webpage content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all(["h1", "h2", "h3"])  

    print("Extracted Titles:")
    for title in titles:
        print(title.get_text())

    # Extract all hyperlinks
    links = soup.find_all("a", href=True)
    print("\nExtracted Links:")
    for link in links:
        print(link["href"])

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
