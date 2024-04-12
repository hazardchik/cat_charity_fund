from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    database_url: str = "sqlite+aiosqlite:///your_database.db"
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()