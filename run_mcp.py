import os
import sys

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.getcwd())

# Import and run the MCP server
from mcp_server import mcp
mcp.run(transport="stdio")
