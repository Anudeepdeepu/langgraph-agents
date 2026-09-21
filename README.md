# Run your Python file
uv run hello.py

# Install LangGraph CLI
uv add "langgraph-cli[inmem]"

# Start the LangGraph development server / Studio
uv run langgraph dev

# Check whether langgraph.json exists
dir langgraph.json

# Show all files in the current folder
dir

# Install colorama (needed for your Windows terminal error)
uv add colorama

# Start LangGraph again after installing colorama
uv run langgraph dev