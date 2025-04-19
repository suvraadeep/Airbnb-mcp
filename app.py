import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def run_memory_chat():
    # Load environment variables
    load_dotenv()
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    # Create MCPClient from config file
    config_file="browser-mcp.json"
    print("Initializing Agent.........")
    client= MCPClient.from_config_file(config_file)

    # Create LLM
    llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")


    # Create agent with the client
    agent = MCPAgent(llm=llm, 
                     client=client, 
                     max_steps=30,
                     memory_enabled=True,)
    print("\n ============INTERACTIVE MCP CLIENT=========")
    print("\n ==========TYPE 'exit' or 'quit' TO EXIT THE APPLICATION===============")
    print("\n ==========TYPE 'clear' TO CLEAR THE CHAT HISTORY==============")
    print("\n ========================")

    try:
        # Main chat loop
        while True:
            # Get user input
            user_input = input("\nYou: ")

            # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

            # Check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

            # Get response from agent
            print("\nAssistant: ", end="", flush=True)

            try:
                # Run the agent with the user input (memory handling is automatic)
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        # Clean up
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
