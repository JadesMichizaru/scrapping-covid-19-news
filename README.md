# SCRAPPING-COVID-19-NEWS
Using Library Python & API Key From https://www.newsapi.org

## Installation
use the package manager [pip](https://pip.pypa.io/en/stable/) to install the library
```bash
        pip install csv

        pip install requests
```

## Usage

``` python
import csv
import requests

# Generate API Key From https://newsapi.org
api_key = "YOUR-API-KEY"
query = "your-query" # Set The Query Here
url = f'https://newsapi.org/v2/everything?q={query}&language=id&pageSize=100&apiKey={api_key}' # This URL can read up to 100 Data
response = requests.get(url) # Get the response from the API
data = response.json() # Convert the response to JSON

articles = data.get('articles', []) # Get the articles from the JSON

# Save to CSV file if You want to analysis your data

with open('your-file-name.csv', mode='w', newline='', encoding='utf-8') as file: # Open the file
    writer = csv.DictWriter(file, fieldnames=['Title', 'Description', 'Source', 'URL']) # Write the headers
    writer.writeheader() # Write the headers

    for article in articles: # Loop through the articles
        writer.writerow({
            'Title': article.get('title'), # Get the title of the article
            'Description': article.get('description'), # Get the description of the article
            'Source': article.get('source', {}).get('name'), # Get the source of the article
            'URL': article.get('url') # Get the URL of the article
        })

print(f"✅ {len(articles)} news saved to your_file_name.csv") # Print the number of news saved to the file
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
