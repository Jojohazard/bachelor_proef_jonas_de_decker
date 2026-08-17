# Input

PDF:
4.jpg

Extraction instruction:
Extract the seller name, seller address, invoice date, invoice total amount, and document reference from the scanned invoice.
Return the result as JSON.

# Configuration

Model:
qwen-3.5-2b

MCP Tool:
ocr-mcp

# Expected Output

{
  "seller_name": "Jhonson-Martin",
  "seller_address": "3836 Moore Ports Nort Micheal MO 018444",
  "invoice_date": "10/29/2016",
  "invoice_total": "797.91$",
  "document_reference": "89969473"
}

# Actual Output

{
  "seller_name": "Jhonson-Martin",
  "seller_address": "3836 Moore Ports Nort Micheal MO 018444",
  "invoice_date": "10/29/2016",
  "invoice_total": "797.91$",
  "document_reference": "89969473"
}

# Time

294s
