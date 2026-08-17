# Input

URL:
https://www.amazon.nl/kindle-paperwhite-2024/dp/B0CFPWLGF2

Extraction instruction:
Extract the screen size, weight, battery life, charging time, and waterproof rating.

# Configuration

Model:
ministral-3-3b

MCP Tool:
playwright & fetch

# Expected Output

{
  "screen_size": "7 inch",
  "weight": "211 g",
  "battery_life": "up to 12 weeks",
  "charging_time": "approximately 2.5 hours",
  "waterproof_rating": "IPX8"
}

# Actual Output

{
  "screen_size": "7 inch",
  "weight": "211 g",
  "battery_life": "up to 12 weeks",
  "charging_time": "2.5 hours",
  "waterproof_rating": "IPX8"
}

# Time

376 seconds
