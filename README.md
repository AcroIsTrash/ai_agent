# Acro's AI Agent
This project is simple langchain agent on the command-line.  It can access tools as well as remember the current conversation.

It uses OpenAI's GPT5 and requests an OPENAI_API_KEY if one isn't currently set in the os environment.  It uses uv to keep track of dependencies within a virtual environment.

**Tools:**
- sum calculator

**Features:**
- cli interface
- conversation memory

# Dependencies
- python 3.13.12
- pip 26.0.1
- uv 0.10.2
- langchain 1.2.10
- langchain-openai 2.21.0

