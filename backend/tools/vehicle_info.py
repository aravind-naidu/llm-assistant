from langchain.tools import tool

@tool
def get_vehicle_status(vehicle_id: str) -> str:
    """
    Fetch latest vehicle status by ID from telemetry DB.
    """
    # Placeholder logic (replace with actual DB/API call)
    return f"Vehicle {vehicle_id} has 78% battery, 120km range, last ping 5 mins ago."

@tool
def rag_tool(query: str) -> str:
    """Retrieve context from vector DB and return relevant info."""
    # You’ll plug in your actual vector DB code here
    return f"RAG context for: {query}"