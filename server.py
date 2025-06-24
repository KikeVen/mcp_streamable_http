from mcp.server.fastmcp import FastMCP
import os
import uvicorn

mcp = FastMCP("HTTP Server", "0.1.0")


@mcp.tool()
def greeting(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
        uvicorn.run(
        mcp,  # Pass the FastMCP instance directly if it implements ASGI, or replace with the correct attribute
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )