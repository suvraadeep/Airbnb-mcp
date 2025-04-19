# Airbnb MCP

This repository demonstrates how to integrate Airbnb MCP servers with LangChain and Groq using a browser-based interface.

---

## To Set It Up From Scratch

### Step 0: initiate uv
```bash
pip install uv
```

### Step 1: Initialize the Project  
```bash
uv init Airbnb-mcp
```

### Step 2: Navigate into the Project  
```bash
cd Airbnb-mcp
```

### Step 3: Create and Activate Conda Environment  
```bash
conda create -n Airbnb-mcp python=3.10
conda activate Airbnb-mcp
```

### Step 4: Install Dependencies  
```bash
uv add langchain-groq
uv add mcp-use
```

### Step 5: Open the Project in Cursor (Make sure you have Cursor installed)  
```bash
cursor .
```

### Step 6: Create a `browser-mcp.json` File  

**Prerequisite**: Make sure Node.js is installed on your machine.

Create a `browser-mcp.json` file in your root directory with the following content:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb"]
    },
    "duckduckgo-search": {
      "command": "npx",
      "args": ["-y", "duckduckgo-mcp-server"]
    }
  }
}
```

This format uses `npx` because the app is based on Node.js.

### Step 7: Add Your API Key

Create a `.env` file and add your Groq API key:
```
GROQ_API_KEY="your_key_here"
```

### Step 8: Run the App  
```bash
python run app.py
```

### Step 9: Configure MCP in Cursor  

1. Open Cursor chat with `Ctrl + L`.
2. Go to `Preferences → Cursor Settings → MCPs`.
3. Add a new **Global MCP Server**.
4. Copy and paste your `browser-mcp.json` content into the configuration box.
5. Restart Cursor IDE.

You're all set 🎉

---

## To Use From This Repository

### Step 1: Clone the Repo  
```bash
git clone https://github.com/suvraadeep/Airbnb-mcp.git
```

### Step 2: Navigate Into the Project  
```bash
cd Airbnb-mcp
```

### Step 3: Create and Activate Conda Environment  
```bash
conda create -n Airbnb-mcp python=3.10
conda activate Airbnb-mcp
```

### Step 4: Open Project in Cursor  
```bash
cursor .
```

### Step 5: Add Your API Key  
Create a `.env` file and insert:
```
GROQ_API_KEY="your_key_here"
```

### Step 6: Install Dependencies  
```bash
uv add langchain-groq
uv add mcp-use
```

### Step 7: Run the App  
```bash
python run app.py
```
