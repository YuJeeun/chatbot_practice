from pydantic import ConfigDict

class Settings(ConfigDict):
    openai_api_key: str
    langchain_project: str
    service_key: str

    class Config:
        env_file = ".env"

settings = Settings()

def get_settings():
    return settings

