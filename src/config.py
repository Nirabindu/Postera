from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Load ENV Files.

    Args:
        BaseSettings (_type_): _description_

    """

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    model_config = SettingsConfigDict(env_file=".env.dev", extra="ignore")

    @property
    def database_url(self) -> str:
        """Db Url.

        Returns:
            str: return a db connection string.

        """
        return (
            f"postgresql+asyncpg://{self.DATABASE_USER}:"
            f"{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/"
            f"{self.DATABASE_NAME}"
        )


Config = Settings()  # type: ignore[call-arg]
