import os
import getpass
import builtins
from langchain.tools import tool
from langchain.agents import create_agent

try:
    from rich.console import Console
    from rich.panel import Panel
    console = Console()
except Exception:
    class _FallbackConsole:
        def print(self, *args, **kwargs):
            return builtins.print(*args, **kwargs)
        def input(self, prompt=""):
            return builtins.input(prompt)
    console = _FallbackConsole()


@tool
def sum(a: float, b: float) -> str:
    """Use whenever finding the sum of exactly 2 numbers"""
    console.print("[yellow]Tool has been called.[/yellow]")
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

    console.print(Panel("Welcome! I'm your AI assistant. Type 'quit' to exit.", title="AI Agent", style="bold green"))
    while True:
        # get input from user
        user_input = console.input("\n[bold cyan]You:[/bold cyan] ").strip()
        if user_input == 'quit':
            break
        messages.append({"role": "user", "content": user_input})
        # get ai response
        console.print("\n[bold green]Assistant:[/bold green] ", end="")
        for chunk in agent.stream({"messages": messages},stream_mode="updates"):
            for step, data in chunk.items():
                for message in data['messages']:
                    messages.append(message)
                    console.print(message.content, end="")
        console.print()


if __name__ == "__main__":
    main()
