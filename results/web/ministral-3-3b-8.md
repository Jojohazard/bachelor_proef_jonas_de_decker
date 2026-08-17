# Input

URL:
https://en.wikipedia.org/wiki/Internet

Extraction instruction:
Extract the year in which the ARPANET was established, the year the Internet protocol suite became widely adopted, and the main protocols in the Internet protocol suite.

# Configuration

Model:
ministral-3-3b

MCP Tool:
playwright & fetch

# Expected Output

{
  "arpanet_established": "1969",
  "protocol_suite": "TCP/IP",
  "main_protocols": [
    "TCP",
    "IP",
    "HTTP",
    "DNS"
  ]
}

# Actual Output

{
  "arpanet_established": "1969",
  "protocol_suite": "TCP/IP",
  "main_protocols": [
    "TCP",
    "IP",
    "HTTP"
  ]
}

# Time

203s
