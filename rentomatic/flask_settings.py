class Config:
    """Base configuration."""


class ProdConfig(Config):
    """Production configuration."""

    ENV = "production"
    DEBUG = False


class DevConfig(Config):
    """Development congifuration."""

    ENV = "development"
    DEBUG = True


class TestConfig(Config):
    """Test Configuration."""

    ENV = "test"
    TESTING = True
    DEBUG = True
