from openai import AzureOpenAI
from config import endpoint, subscription_key
# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    api_key=subscription_key,
    api_version="...",
    azure_endpoint=endpoint,
)

# completion = client.chat.completions.create(
#     model="deployment-name",  # e.g. gpt-35-instant
#     messages=[
#         {
#             "role": "user",
#             "content": "How do I output all files in a directory using Python?",
#         },
#     ],
# )
# print(completion.to_json())