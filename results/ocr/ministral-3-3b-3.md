# Input

PDF:
3.jpg

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
  "seller_name": "Flitzpartick and Sons",
  "seller_address": "00480 Cook Cove Spencerport, UT 12036",
  "invoice_date": "03/03/2012",
  "invoice_total": "6860.45$",
  "document_reference": "124827181"
}

# Actual Output

{
  "seller_name": "Flitzpartick and Sons",
  "seller_address": "00480 Cook Cove Spencerport, UT 12036",
  "invoice_date": "03/03/2012",
  "invoice_total": "6860.45$",
  "document_reference": "124827181"
}
# Time

388s
