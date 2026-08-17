# Input

URL:
https://www.nasa.gov/

Extraction instruction:
Extract the organization name, its main purpose, and three areas of activity mentioned on the website.

# Configuration

Model:
ministral-3-3b

MCP Tool:
playwright & fetch

# Expected Output

{
  "organization": "NASA",
  "purpose": "Explore the unknown in air and space, innovate for the benefit of humanity, and inspire the world through discovery",
  "activities": [
    "Space exploration",
    "Earth science",
    "Aeronautics"
  ]
}

# Actual Output

{
  "organization": "NASA",
  "purpose": "Exploring space and conducting scientific research",
  "activities": [
    "Space exploration",
    "Earth science"
  ]
}

# Time

378s
