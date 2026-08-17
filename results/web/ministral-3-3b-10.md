# Input

URL:
https://www.adobe.com/products/acrobat.html

Extraction instruction:
Extract the product name, its main purpose, and three features mentioned on the page.

# Configuration

Model:
nvidia/nemotron-3-nano

MCP Tool:
playwright & fetch

# Expected Output

{
  "product": "Adobe Acrobat",
  "purpose": "Create, edit, sign, share, and manage PDF documents",
  "features": [
    "PDF editing",
    "Electronic signatures",
    "Document sharing"
  ]
}

# Actual Output

{
  "product": "Adobe Acrobat",
  "purpose": "Create, edit, and manage PDF documents",
  "features": [
    "PDF editing",
    "Electronic signatures",
    "Document sharing"
  ]
}

# Time

286s
