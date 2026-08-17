from openai import OpenAI
import app.config as config

def getClient() -> OpenAI:
    return OpenAI(base_url=f"{config.LM_STUDIO_URL}/v1",api_key=config.API_KEY)