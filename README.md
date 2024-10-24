# Article Scraper

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=open-source-initiative)

## **Project Overview**

The Article Scraper is a Python application designed to extract article information from specified URLs. It captures details such as titles, categories, publication dates, and content while preserving essential HTML tags.

## ✨ **Features**

- **Multi-Article Scraping**: Access and scrape data from multiple articles within the same domain.
- **Data Cleaning**: Extracts only relevant content, leaving necessary HTML tags (`<h2>`, `<h3>`, `<p>`, `<strong>`).
- **Error Handling**: Automatically handles pages with poorly configured SSR by using Selenium for JS rendering.
- **Output**: Saves the scraped data into response.json in a structured JSON format.

## 💾 Installation

### 📂 Clone the Repository

```bash
git clone https://github.com/MaximPyanin/Zadanie-rekrutacyjne-Python-Sta-.git
```

### 🔐 Set Up Environment Variables
Create a .env file in the root directory of the project and add the following environment variables:

- BASE_URL=your_base_url
- ARTICLE_ONE=your_atricle_one
- ARTICLE_TWO=your_article_two

Install Dependencies
```bash
poetry install
```

### 🧹 Linter and Formatter
To format the code, run:
```bash
poetry run ruff format
```

To check for linting issues and automatically fix them, use:
```bash
poetry run ruff check --fix
```
### 🔧 Usage
Run the Application
To start the application, use the following command:

```bash
poetry run python main.py
```

### 📄   License
This project is licensed under the MIT License - see the LICENSE file for details.