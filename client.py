"""
Client script for Customer Support CrewAI API
Demonstrates how to interact with the FastAPI endpoints
"""

import requests
import json
from typing import Dict, Any


class CustomerSupportClient:
    """Client for interacting with the Customer Support CrewAI API."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Initialize the client.
        
        Args:
            base_url: Base URL of the API server (default: http://localhost:8000)
        """
        self.base_url = base_url.rstrip('/')
    
    def health_check(self) -> Dict[str, Any]:
        """Check if the API is healthy."""
        try:
            response = requests.get(f"{self.base_url}/health")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def get_api_info(self) -> Dict[str, Any]:
        """Get API information from root endpoint."""
        try:
            response = requests.get(f"{self.base_url}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
    
    def process_inquiry(
        self, 
        customer: str, 
        person: str, 
        inquiry: str
    ) -> Dict[str, Any]:
        """
        Process a customer support inquiry.
        
        Args:
            customer: Name of the customer company
            person: Name of the person making the inquiry
            inquiry: The customer's question or request
        
        Returns:
            Dictionary containing the response or error
        """
        url = f"{self.base_url}/support/inquiry"
        payload = {
            "customer": customer,
            "person": person,
            "inquiry": inquiry
        }
        
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            try:
                error_detail = response.json()
                return {"error": error_detail.get("detail", str(e))}
            except:
                return {"error": str(e)}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}


def print_response(title: str, response: Dict[str, Any]):
    """Pretty print API responses."""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print(json.dumps(response, indent=2))
    print(f"{'='*60}\n")


def main():
    """Main function demonstrating API usage."""
    # Initialize client
    client = CustomerSupportClient()
    
    print("Customer Support CrewAI API Client")
    print("=" * 60)
    
    # 1. Health check
    print("\n1. Checking API health...")
    health = client.health_check()
    print_response("Health Check Response", health)
    
    # 2. Get API info
    print("2. Getting API information...")
    api_info = client.get_api_info()
    print_response("API Information", api_info)
    
    # 3. Process sample inquiry
    print("3. Processing sample customer support inquiry...")
    sample_inquiry = client.process_inquiry(
        customer="DeepLearningAI",
        person="Andrew Ng",
        inquiry="I need help with setting up a Crew and kicking it off, "
                "specifically how can I add memory to my crew? "
                "Can you provide guidance?"
    )
    print_response("Support Inquiry Response", sample_inquiry)
    
    # 4. Process another sample inquiry
    print("4. Processing another sample inquiry...")
    another_inquiry = client.process_inquiry(
        customer="TechCorp",
        person="Jane Smith",
        inquiry="What are the best practices for creating agents in CrewAI? "
                "I want to build a customer service bot."
    )
    print_response("Second Support Inquiry Response", another_inquiry)
    
    print("\nClient demonstration complete!")


if __name__ == "__main__":
    main()

