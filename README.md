# Customer Support CrewAI API

A FastAPI-based REST API for processing customer support inquiries using CrewAI. This application uses AI agents to provide intelligent, comprehensive responses to customer questions.

## Features

- 🤖 **AI-Powered Support**: Uses CrewAI agents to process customer inquiries
- 🔍 **Web Scraping**: Automatically scrapes documentation to find relevant information
- ✅ **Quality Assurance**: Two-agent system ensures high-quality responses
- 🚀 **FastAPI REST API**: Modern, fast, and well-documented API
- 🐳 **Docker Support**: Easy deployment with Docker
- 📝 **Interactive Documentation**: Auto-generated API docs with Swagger UI

## Architecture

The application uses a two-agent CrewAI system:

1. **Senior Support Representative**: Primary agent that handles customer inquiries
2. **Support Quality Assurance Specialist**: Reviews and improves responses before sending

## Project Structure

```
.
├── main.py              # Core CrewAI logic and crew creation
├── app.py               # FastAPI application and endpoints
├── client.py            # Comprehensive API client with examples
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md           # This file
```

## Prerequisites

- Python 3.11 or higher
- API keys for:
  - LLM provider (OpenAI, Anthropic, etc.)
  - SerperDev (for web search, if using SerperDevTool)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd L3_Customer_Support_CewAI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
# LLM Provider (choose one)
OPENAI_API_KEY=your_openai_api_key
# OR
ANTHROPIC_API_KEY=your_anthropic_api_key

# SerperDev (for web search)
SERPER_API_KEY=your_serper_api_key

# Optional: Other CrewAI configuration
```

## Usage

### Running the API Server

#### Option 1: Direct Python execution

```bash
python app.py
```

#### Option 2: Using uvicorn

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Running with Docker

#### Build the image

```bash
docker build -t customer-support-crewai .
```

#### Run the container

```bash
docker run -p 8000:8000 --env-file .env customer-support-crewai
```

### Using the Client

#### Run the comprehensive client example

```bash
python client.py
```

#### Run the simple example

```bash
python example_request.py
```

#### Use the client in your code

```python
from client import CustomerSupportClient

client = CustomerSupportClient(base_url="http://localhost:8000")

# Check API health
health = client.health_check()
print(health)

# Process an inquiry
result = client.process_inquiry(
    customer="YourCompany",
    person="John Doe",
    inquiry="How do I set up CrewAI?"
)
print(result)
```

## API Endpoints

### `GET /`

Get API information and available endpoints.

**Response:**
```json
{
  "message": "Customer Support CrewAI API",
  "version": "1.0.0",
  "endpoints": {
    "health": "/health",
    "support": "/support/inquiry"
  }
}
```

### `GET /health`

Health check endpoint to verify the API is running.

**Response:**
```json
{
  "status": "healthy",
  "service": "customer-support-crewai"
}
```

### `POST /support/inquiry`

Process a customer support inquiry.

**Request Body:**
```json
{
  "customer": "CompanyName",
  "person": "PersonName",
  "inquiry": "Your question or request here"
}
```

**Response:**
```json
{
  "success": true,
  "response": "Detailed response from the AI agents..."
}
```

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/support/inquiry" \
  -H "Content-Type: application/json" \
  -d '{
    "customer": "DeepLearningAI",
    "person": "Andrew Ng",
    "inquiry": "How can I add memory to my crew?"
  }'
```

## API Documentation

Once the server is running, you can access interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Running the Original Script

You can still run `main.py` directly as a standalone script:

```bash
python main.py
```

This will process a default example inquiry.

## Configuration

### Environment Variables

The application uses the following environment variables (configured in `.env`):

- `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`: LLM provider API key
- `SERPER_API_KEY`: SerperDev API key for web search
- Other CrewAI-specific environment variables as needed

### Customizing the Crew

You can modify the agents, tasks, and tools in `main.py`:

- **Agents**: Customize roles, goals, and backstories
- **Tasks**: Adjust task descriptions and expected outputs
- **Tools**: Add or modify tools (e.g., different website scrapers)

## Development

### Project Dependencies

Key dependencies include:
- `crewai`: AI agent framework
- `crewai-tools`: Tools for CrewAI agents
- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `python-dotenv`: Environment variable management
- `requests`: HTTP client (for client scripts)

See `requirements.txt` for the complete list.

## Troubleshooting

### API Connection Errors

- Ensure the API server is running before using the client
- Check that the port (8000) is not already in use
- Verify the base URL in client scripts matches your server

### Environment Variable Issues

- Make sure your `.env` file is in the project root
- Verify all required API keys are set correctly
- Check that API keys have proper permissions

### Docker Issues

- Ensure Docker is installed and running
- Verify the `.env` file exists when using `--env-file`
- Check Docker logs: `docker logs <container-id>`

## License

This project is licensed under the Apache 2.0 License. 

## Support

For issues and questions, please open an issue in the repository.

