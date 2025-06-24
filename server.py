from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("HTTP Server", "0.1.0")


@mcp.tool()
def greeting(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=int(os.environ.get("PORT", 8000))) # type: ignore