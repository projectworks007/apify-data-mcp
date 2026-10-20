"""Magicbricks India property listings API - LangChain tool example.

Wraps the "magicbricks-properties" Apify actor as a LangChain tool and lets an agent use it.
Actor page: https://apify.com/highbrow_fame/magicbricks-properties

    pip install langchain-apify langchain langgraph langchain-openai
    export APIFY_TOKEN=...      # https://console.apify.com/account/integrations
    export OPENAI_API_KEY=...   # or use any other chat model
    python langchain_tool.py
"""
import os

# langchain-apify reads APIFY_API_TOKEN; reuse APIFY_TOKEN so one variable is enough.
os.environ.setdefault("APIFY_API_TOKEN", os.environ["APIFY_TOKEN"])

from langchain.chat_models import init_chat_model
from langchain_apify import ApifyActorsTool
from langgraph.prebuilt import create_react_agent

# The agent fills `run_input` with the actor input. Example input:
# {'places': ['Pune'], 'transaction': 'sale', 'propertyType': 'flat', 'bedrooms': ['2', '3'], 'maxListingsPerSearch': 50, 'sortBy': 'newest'}
tool = ApifyActorsTool("highbrow_fame/magicbricks-properties")

# Direct call without an LLM:
# run_input = <the example input above>
# items = tool.invoke({"run_input": run_input})

llm = init_chat_model(
    os.environ.get("MODEL", "gpt-4o-mini"),
    model_provider=os.environ.get("MODEL_PROVIDER", "openai"),
)
agent = create_react_agent(llm, [tool])

result = agent.invoke({"messages": [("user", "Find 3 BHK flats for sale in Whitefield, Bangalore and show the cheapest five.")]})
print(result["messages"][-1].content)
