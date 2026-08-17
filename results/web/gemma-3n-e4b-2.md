# Input

URL:
https://www.mozilla.org/

Extraction instruction:
Extract the organization name, website purpose, and three main products or services.

# Configuration

Model:
gemma-3n-e4b

MCP Tool:
playwright & fetch

# Expected Output

{
  "organization": "Mozilla",
  "purpose": "Building an open and accessible internet",
  "products": [
    "Firefox",
    "Mozilla VPN",
    "Mozilla Monitor"
  ]
}

# Actual Output

{
  "organization": "Mozilla",
  "purpose": "Web browser company",
  "products": [
    "Firefox",
    "Mozilla VPN"
  ]
}

# Time

567s