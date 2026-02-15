import os, getpass
from langchain.tools import tool
from langchain.agents import create_agent

@tool
def sum(a: float, b: float) -> str:
    """Useful for finding the sum of exactly 2 numbers"""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}\n"

def main():
    # get OpenAI api key from user if not set in the environment
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
    
    # get tools
    tools = [sum]
    # create an ai agent
    agent = create_agent(
        model="gpt-5-nano",
        tools= tools
    )
    # save messages so the ai can remember what has been said before
    messages = []

    print("Welcome! I'm your AI assistant.  Type 'quit' to exit.")
    while True:
        # get input from user
        user_input = input("\nYou: ").strip()
        if user_input == 'quit':
            break
        messages.append({"role": "user", "content": user_input})
        # get ai response
        print("\nAssistant: ", end="")
        for chunk in agent.stream({"messages": messages},stream_mode="updates"):
            for step, data in chunk.items():
                #print(f"step: {step}")
                #print(f"content: {data['messages'][-1].content_blocks}")
                for message in data['messages']:
                    messages.append(message)
                    print(message.content, end="")
        print()


if __name__ == "__main__":
    main()
