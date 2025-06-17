import os
from dotenv import load_dotenv

load_dotenv()

env_variables = {
    "modelApiKey" : os.environ.get("MODELAI_API_KEY")
}