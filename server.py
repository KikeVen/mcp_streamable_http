
from fastmcp import FastMCP

# Create the FastMCP instance
mcp = FastMCP("HTTP Server", "0.1.0")

@mcp.tool()
def greeting(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Use FastMCP's built-in run method
    mcp.run(transport="http", host="0.0.0.0", port=8000)