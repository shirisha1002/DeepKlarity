import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_bbc():
    url = 'https://www.bbc.com/news/world/asia'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    # Updated selector for the title and summary
    for item in soup.find_all('div', class_='sc-b8778340-3 gxEarx'):
        title_tag = item.find('h2', class_='sc-1207bea1-3 fxdkXN')
        summary_tag = item.find('p', class_='sc-b8778340-4 kYtujW')
        
        if title_tag:
            title = title_tag.get_text()
            summary = summary_tag.get_text().replace('\xa0', ' ') if summary_tag else 'No Summary'  # Get summary if available
            publication_date = datetime.now().strftime('%Y-%m-%d')  # Placeholder for actual date
            source = 'BBC'
            
            # Check if the anchor tag exists for the link
            link_tag = title_tag.find_parent('a')
            if link_tag and 'href' in link_tag.attrs:
                link = link_tag['href']
            else:
                link = None  # or you can set a default value or skip this article
            
            articles.append([title, summary, publication_date, source, link])
    return articles


def save_to_csv(articles):
    with open('news_articles.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Summary', 'Publication Date', 'Source', 'URL'])
        writer.writerows(articles)

if __name__ == "__main__":
    articles = scrape_bbc()
    if articles:  # Only save if there are articles
        save_to_csv(articles)
    else:
        print("No articles found to save.")