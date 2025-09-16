"""Main entry point for the AAS MCP server."""

from aas_mcp.server import cli_main


def main() -> None:
    """Entry point for running the AAS MCP server as a module."""
    cli_main()


if __name__ == "__main__":
    main()
