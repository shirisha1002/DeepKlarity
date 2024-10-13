# News Aggregator API

## Overview
This project is a news aggregator that scrapes articles, categorizes them using NLP, and serves them via a REST API built with FastAPI.

## Features
- Scrape news articles from BBC.
- Categorize articles into topics like politics, technology, and sports.
- Serve articles through a REST API with endpoints for retrieval and search.

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/{yourusername}/news-aggregator.git
   cd news-aggregator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```

## API Endpoints
- **GET /articles**: Retrieve all articles, with optional filtering by category and date range.
- **GET /articles/{id}**: Retrieve a specific article by ID.
- **GET /search**: Search articles by keywords.

## Usage Examples
- Retrieve all articles: `GET http://127.0.0.1:5000/articles`
- Retrieve articles by category: `GET http://127.0.0.1:5000/articles?category=Politics`
- Retrieve a specific article: `GET http://127.0.0.1:5000/articles/1`
- Search articles: `GET http://127.0.0.1:5000/search?keyword=BJP`

## Postman Collection
Import the `postman_collection.json` file into Postman to test the API endpoints.

## Media
Screenshots and a video demonstration of the API in action are available in the `media/` directory.

## Documentation
The code is documented with comments explaining the functionality of each part. Refer to the code files for detailed documentation.

## Evaluation Criteria
- Scraper robustness and data quality.
- API design and functionality.
- Error handling of different scenarios.
- Code structure and documentation.