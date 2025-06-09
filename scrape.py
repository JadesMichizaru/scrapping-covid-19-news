import requests
import csv

# Change API Key from https://newsapi.org
api_key = 'YOUR-API-KEY'
query = 'covid-19'  # Set The Query Here
url = f'https://newsapi.org/v2/everything?q={query}&language=id&pageSize=100&apiKey={api_key}'

response = requests.get(url)
data = response.json()

articles = data.get('articles', [])

# Save to CSV File
with open('your-file-name.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Caption', 'Description', 'Source', 'URL'])
    writer.writeheader()

    for article in articles:
        writer.writerow({
            'Caption': article.get('title'),
            'Description': article.get('description'),
            'Source': article.get('source', {}).get('name'),
            'URL': article.get('url')
        })

print(f"✅ {len(articles)} news saved to covid_19_news.csv")
