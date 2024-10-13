import pandas as pd
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define keywords for categorization
categories = {
    'Politics': ['democracy', 'elections', 'government', 'policy', 'legislation', 'political party', 'candidate', 'campaign', 'voting', 'constitution', 'diplomacy', 'foreign policy', 'public opinion', 'debate', 'lobbying', 'civil rights', 'human rights', 'national security', 'corruption', 'political reform', 'BJP', 'Indian National Congress', 'AAP'],
    'Technology': ['technology', 'artificial intelligence', 'machine learning', 'data science', 'blockchain', 'cloud computing', 'cybersecurity', 'internet of things', '5G', 'automation', 'augmented reality', 'virtual reality', 'quantum computing', 'devops', 'software development', 'mobile applications', 'web development', 'APIs', 'SaaS', 'big data', 'fintech'],
    'Sports': ['athlete', 'team', 'competition', 'tournament', 'match', 'score', 'win', 'loss', 'championship', 'league', 'playoff', 'goal', 'coach', 'training', 'fitness', 'stadium', 'injury', 'record', 'strategy', 'fan'],
    'Business': ['entrepreneurship', 'startup', 'revenue', 'profit', 'market analysis', 'investment', 'stock market', 'shares', 'venture capital', 'branding', 'marketing', 'sales', 'customer relationship', 'supply chain', 'logistics', 'leadership', 'management', 'corporate governance', 'innovation', 'e-commerce']
}

def categorize_article(text):
    # Convert text to lowercase for matching
    text_lower = text.lower()
    
    # Check for keywords in the text
    for category, keywords in categories.items():
        if any(keyword in text_lower for keyword in keywords):
            return category
    return 'General'

# Load the existing CSV file
df = pd.read_csv('news_articles.csv', encoding='Windows-1252')
df['id'] = [str(i) for i in range(1, len(df) + 1)]

columns = ['id'] + [col for col in df.columns if col != 'id']
df = df[columns]
# Categorize each article based on the summary
df['Category'] = df['Summary'].apply(categorize_article)

# Save the updated DataFrame back to CSV
df.to_csv('news_articles.csv', index=False, encoding='utf-8')