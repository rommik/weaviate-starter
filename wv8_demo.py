# Connects to Weaviate Demo instance and prints meta info
import weaviate
import os
import json
from dotenv import load_dotenv

load_dotenv()
# Only if authentication enabled; assuming API key authentication
auth_config = weaviate.AuthApiKey(api_key='readonly-demo')  # Replace w/ your Weaviate instance API key

# Instantiate the client
client = weaviate.Client(
    url='https://edu-demo.weaviate.network',
    auth_client_secret=auth_config,  # Only necessary if authentication enabled
    additional_headers={        
        "X-OpenAI-Api-Key": os.getenv('OPENAI_API_KEY'),            # Replace with your OpenAI key
    }
)

meta_info = client.get_meta()
print(json.dumps(meta_info, indent=2))

# Get Example
# res = client.query.get(
#     "WikiCity", ["city_name", "country", "lng", "lat"]
# ).with_near_text({
#     "concepts": ["Major Japanese city"]
# }).with_limit(5).do()

# print(json.dumps(res, indent=2))

## Ask example
# ask = {
#   "question": "When was the London Olympics?",
#   "properties": ["wiki_summary"]
# }

# res = (
#   client.query
#   .get("WikiCity", [
#       "city_name",
#       "_additional {answer {hasAnswer property result} }"
#   ])
#   .with_ask(ask)
#   .with_limit(1)
#   .do()
# )
#print(json.dumps(res, indent=2))

## GenAI example
res = client.query.get(
    "WikiCity", ["city_name", "wiki_summary"]
).with_near_text({
    "concepts": ["Popular Southeast Asian tourist destination"]
}).with_limit(3).with_generate(
    single_prompt=\
    "Write a tweet with a potentially surprising fact from {wiki_summary}"
).do()

for city_result in res["data"]["Get"]["WikiCity"]:
    print(json.dumps(city_result["_additional"], indent=2))