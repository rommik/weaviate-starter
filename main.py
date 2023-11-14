import weaviate
import os
from dotenv import load_dotenv
import json
load_dotenv()
# Only if authentication enabled; assuming API key authentication
auth_config = weaviate.AuthApiKey(api_key=os.getenv('WV8_API_KEY'))  # Replace w/ your Weaviate instance API key

# Instantiate the client
client = weaviate.Client(
    url=os.getenv('WV8_CLUSTER_URI'),
    auth_client_secret=auth_config,  # Only necessary if authentication enabled
    additional_headers={        
        "X-OpenAI-Api-Key": os.getenv('OPENAI_API_KEY'),            # Replace with your OpenAI key
    }
)

meta_info = client.get_meta()
print(json.dumps(meta_info, indent=2))