# Input

URL:
https://www.python.org/

Extraction instruction:
Extract the website name, page title, main purpose, and programming language.

# Configuration

Model:
ministral-3-3b

MCP Tool:
playwright & fetch

# Expected Output

{
  "website_name": "Python.org",
  "page_title": "Welcome to Python.org",
  "main_purpose": "Provide information and resources about Python",
  "programming_language": "Python"
}

# Actual Output

{
  "website_name": "Python.org",
  "page_title": "Welcome to Python.org",
  "main_purpose": "Programming language and developer resources",
  "programming_language": "Python"
}

# Time

318s
