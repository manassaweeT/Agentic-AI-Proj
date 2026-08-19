from config import endpoint, subscription_key, model_name
from openai import AsyncOpenAI
from agents import set_default_openai_client

client = AsyncOpenAI(
    default_headers={
        "api-key": subscription_key,
    },
    api_key=subscription_key,
    base_url=endpoint
)

set_default_openai_client(client)
