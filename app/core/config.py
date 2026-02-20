from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    app_name: str = Field(..., description='The name of the application')
    environment: str = Field(..., description='The environment the app is running in')
    debug: bool = Field(False, description='Enable debugging mode')
    database_url: str = Field(..., env='DATABASE_URL')
    api_key: str = Field(..., env='API_KEY')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()