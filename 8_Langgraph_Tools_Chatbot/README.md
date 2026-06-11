human : Enter your expense question: whats the expenses in month of december from dec 1 to dec 19

ai : Here's a summary of your expenses for December 1-19:

**Total Expenses:** $1,591.65

**Breakdown:**
- **Dec 1** (Rent): Apartment rent - $1,200.00  
- **Dec 6** (Groceries): Weekly groceries - $104.90  
- **Dec 12** (Transport): Fuel - $46.75  
- **Dec 18** (Gifts): Holiday gifts - $240.00  

Let me know if you'd like further analysis or details!

## What this example does

This folder shows two ways to use tools with LangGraph.

The first example is a simple tools chatbot. It gives the model two Python tools: one to add numbers and one to multiply numbers. The graph sends the user message to the model, checks whether the model wants to call a tool, runs the tool when needed, and then sends the tool result back to the model so it can answer.

The second example uses MCP. MCP means Model Context Protocol. In simple terms, it lets the chatbot use tools that are served by a separate server instead of tools written directly inside the chatbot file.

## Files in this folder

`8_Langgraph_Tools_chatbot.ipynb` is the notebook version of the basic tools chatbot. It shows how to create add and multiply tools, bind them to the LLM, add a `ToolNode`, and route tool calls in LangGraph.

`chatbot.py` is the Python script version of the basic tools chatbot. It creates the same add and multiply tools and builds a LangGraph graph around them. It also shows streaming with `graph.stream()`.

`streamlit_frontend.py` is a small Streamlit UI for the tools chatbot. It shows a chat box in the browser, keeps chat history in `st.session_state`, sends the messages to the graph, and streams the assistant response back to the page.

`mcp_server.py` is the local FastMCP server. It has hardcoded expense data for every month from January to December. It exposes expense tools that another program can call.

`mcp.py` is the MCP client and LangGraph chatbot. It connects to `mcp_server.py`, loads the tools from that server, binds those tools to the LLM, and lets you ask expense questions from the terminal.

## MCP server tools

The MCP server provides these tools:

- `get_expenses_for_month`: returns all expenses for one month.
- `get_expenses_between_days`: returns expenses between a start day and end day in one month.
- `get_weekly_cost_for_month`: returns week-by-week totals for one month.

The month can be written in short form or full form. For example, `Nov` and `November` both work.

## How the MCP flow works

First, `mcp_server.py` starts a local FastMCP server over stdio. This server owns the hardcoded expense data and exposes the expense tools.

Then, `mcp.py` starts a `MultiServerMCPClient`. That client points to the local `mcp_server.py` file and asks it for available tools.

After the tools are loaded, `mcp.py` binds them to the Groq chat model. The LangGraph graph then works like this:

1. The user types an expense question in the terminal.
2. The question is added as a `HumanMessage`.
3. The model decides whether it needs an expense tool.
4. If a tool is needed, `ToolNode` runs the correct MCP tool.
5. The tool result goes back to the model.
6. The model writes the final answer in simple text.

## How to run

Run the MCP expense chatbot from the project root:

```powershell
python 8_Langgraph_Tools_Chatbot/mcp.py
```

Then type a question like:

```text
what are my december expenses from dec 1 to dec 19
```

You can also ask:

```text
show weekly cost for november
```

or:

```text
what are all expenses for march
```

## Important note

The expense data is hardcoded. It is sample data only. The chatbot is not reading a real bank account, database, or spreadsheet.
