from google.adk.agents.llm_agent import Agent
import random

def get_weather(city: str) -> dict:
    """
    Returns weather information for a specified city.

    Args:
        city: The name of the city (e.g., 'New York', 'London', 'Tokyo')

    Returns:
        A dictionary with weather information including temperature and conditions
    """
    # Simulated weather data for demonstration
    conditions = ['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy', 'Overcast', 'Clear']
    temperature_c = random.randint(10, 30)
    temperature_f = int((temperature_c * 9/5) + 32)
    humidity = random.randint(40, 90)
    wind_speed = random.randint(5, 25)

    return {
        "status": "success",
        "city": city,
        "temperature_celsius": f"{temperature_c}°C",
        "temperature_fahrenheit": f"{temperature_f}°F",
        "condition": random.choice(conditions),
        "humidity": f"{humidity}%",
        "wind_speed": f"{wind_speed} km/h",
        "note": "This is simulated weather data for demonstration purposes"
    }

def search_information(query: str) -> dict:
    """
    Searches for information based on a query.

    Args:
        query: The search query string

    Returns:
        A dictionary with search results
    """
    # Simulated search results for demonstration
    sample_results = {
        "gemini": "Gemini is Google's most capable AI model family, designed for multimodal understanding.",
        "weather": "Weather refers to the state of the atmosphere at a given time and place.",
        "python": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
        "ai": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines.",
    }

    # Simple keyword matching
    query_lower = query.lower()
    for keyword, description in sample_results.items():
        if keyword in query_lower:
            return {
                "status": "success",
                "query": query,
                "result": description,
                "source": "Simulated knowledge base"
            }

    return {
        "status": "success",
        "query": query,
        "result": f"Information about '{query}' - this is a simulated search result.",
        "source": "Simulated knowledge base"
    }

# Create the root agent with weather and search tools
root_agent = Agent(
    model='gemini-2.0-flash-exp',
    name='weather_search_assistant',
    description="A helpful assistant that can provide weather information and search for general knowledge",
    instruction="""You are a friendly and helpful assistant with access to weather and search tools.

    - When users ask about weather in a city, use the 'get_weather' tool
    - When users ask general questions or want to search for information, use the 'search_information' tool
    - Provide clear, friendly responses
    - The weather data is simulated for demonstration purposes

    Be conversational and helpful!""",
    tools=[get_weather, search_information],
)
