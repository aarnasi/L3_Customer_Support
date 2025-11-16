"""
Simple example of making a request to the Customer Support CrewAI API
"""

import requests
import json

# API endpoint
url = "http://0.0.0.0:8000/support/inquiry"

# Sample request payload
payload = {
    "customer": "DeepLearningAI",
    "person": "Andrew Ng",
    "inquiry": "I need help with setting up a Crew and kicking it off, "
               "specifically how can I add memory to my crew? "
               "Can you provide guidance?"
}

# Make the request
print("Sending request to Customer Support API...")
print(f"URL: {url}")
print(f"Payload: {json.dumps(payload, indent=2)}")
print("\n" + "="*60 + "\n")

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()
    
    result = response.json()
    
    print("Response received successfully!")
    print(json.dumps(result, indent=2))
    
    if result.get("success"):
        print("\n" + "="*60)
        print("Support Response:")
        print("="*60)
        print(result.get("response", "No response content"))
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
    if response.text:
        print(f"Error details: {response.text}")
except requests.exceptions.ConnectionError:
    print("Connection Error: Could not connect to the API.")
    print("Make sure the API server is running on http://localhost:8000")
except Exception as e:
    print(f"Error: {e}")

