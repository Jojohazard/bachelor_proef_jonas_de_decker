# Input

PDF:
1.jpg

Extraction instruction:
Extract the seller name, seller address, invoice date, invoice total amount, and document reference from the scanned invoice.
Return the result as JSON.

# Configuration

Model:
gemma-3n-e4b

MCP Tool:
ocr-mcp

# Expected Output

{
  "seller_name": "Andrews, Kirby, Valdez",
  "seller_address": "58861 Gonzalez Prairie Lake Daneillefurt IN 58228",
  "invoice_date": "04/13/2013",
  "invoice_total": "5640.17$",
  "document_reference": "51109338"
}

# Actual Output

{
  "seller_name": "Andrews, Kirby, Valdez",
  "seller_address": "58861 Gonzalez",
  "invoice_date": "04/13/2013",
  "invoice_total": "5640.17",
  "document_reference": "51109338"
}

# Time

553s
