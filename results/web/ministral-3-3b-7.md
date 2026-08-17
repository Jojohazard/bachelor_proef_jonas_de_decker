# Input

URL:
https://www.amazon.nl/kindle-paperwhite-2024/dp/B0CFPWLGF2

Extraction instruction:
Extract all supported document and image file formats mentioned on the product page.

# Configuration

Model:
ministral-3-3b

MCP Tool:
playwright & fetch

# Expected Output

{
  "formats": [
    "AZW3",
    "AZW",
    "TXT",
    "PDF",
    "MOBI",
    "PRC",
    "DOCX",
    "DOC",
    "HTML",
    "EPUB",
    "RTF",
    "JPEG",
    "GIF",
    "PNG",
    "BMP"
  ]
}

# Actual Output

{
  "formats": [
    "AZW3",
    "AZW",
    "TXT",
    "PDF",
    "MOBI",
    "DOCX",
    "HTML",
    "EPUB",
    "RTF"
  ]
}

# Time

389s
