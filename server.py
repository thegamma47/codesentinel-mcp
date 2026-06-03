from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CodeSentinel")


@mcp.tool()
def hello_world(name: str) -> str:
    """Say hello to someone. Use this to test if CodeSentinel is working."""
    return f"Hello {name}! CodeSentinel MCP server is live 🚀"


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="sse")