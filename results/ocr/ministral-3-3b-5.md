# Input

PDF:
5.jpg

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
  "seller_name": "Obrien Group",
  "seller_address": "6217 Boyd Ville Apt 758 Robbinsberg, AZ 54997",
  "invoice_date": "12/25/2013",
  "invoice_total": "732.34$",
  "document_reference": "72126555"
}

# Actual Output

{
  "seller_name": "Obrien Group",
  "seller_address": "6217 Boyd Ville Apt 758 Robbinsberg, AZ 54997",
  "invoice_date": "12/25/2013",
  "invoice_total": "732.34$",
  "document_reference": "72126555"
}


# Time

523s
