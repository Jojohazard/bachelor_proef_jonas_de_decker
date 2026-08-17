# Input

PDF:
2.jpg

Extraction instruction:
Extract the seller name, seller address, invoice date, invoice total amount, and document reference from the scanned invoice.
Return the result as JSON.

# Configuration

Model:
ministral-3-3b

MCP Tool:
ocr-mcp

# Expected Output

{
  "client_address": "70391 Kelsey Terrace Graceland. VT 41740",
  "invoice_date": "04/01/2016",
  "invoice_total": "819.06$",
  "document_reference": "16273983"
}

# Actual Output

{
  "client_address": "70391 Kelsey Terrace Graceland. VT 41740",
  "invoice_date": "04/01/2016",
  "invoice_total": "819.06$",
  "document_reference": "16273983"
}

# Time

615s
