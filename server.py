from fastmcp import FastMCP
import uvicorn

# Create the FastMCP instance
fast_mcp = FastMCP("HTTP Server", "0.1.0")

@fast_mcp.tool()
def greeting(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"

# Expose the ASGI app for uvicorn to find
mcp = fast_mcp.http_app()

if __name__ == "__main__":
    uvicorn.run(
        mcp,  # Use the exposed ASGI app
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )