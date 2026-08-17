# Input

URL:
https://www.python.org/

Extraction instruction:
Extract the website name, page title, main purpose, and programming language.

# Configuration

Model:
gemma-3n-e4b

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
  "main_purpose": "Python programming language website",
  "programming_language": "Python"
}

# Time

346s