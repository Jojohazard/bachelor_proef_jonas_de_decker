# Input

URL:
https://www.amazon.nl/kindle-paperwhite-2024/dp/B0CFPWLGF2

Extraction instruction:
Extract the product name, brand, price, rating, and storage capacity.

# Configuration

Model:
qwen-3.5-2b


MCP Tool:
playwright & fetch

# Expected Output

{
  "product_name": "Amazon Kindle Paperwhite",
  "brand": "Amazon",
  "price": "€179.99",
  "rating": "4.5",
  "storage": "16 GB"
}

# Actual Output

{
  "product_name": "Amazon Kindle Paperwhite",
  "brand": "Amazon",
  "price": "€179.99",
  "rating": "4.5",
  "storage": "16 GB"
}

# Time

301.4s
