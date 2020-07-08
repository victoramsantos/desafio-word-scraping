import configparser
import os

from src.library.logger.Logger import Logger

if __name__ == "__main__":
    configuration = configparser.ConfigParser()
    configuration.read("./application.ini")

    environment: str = os.getenv("ENVIRONMENT", "DEV")
    Logger.info(f"Running with environment: {environment}")

    for key, value in configuration[environment].items():
        if not os.getenv(key.upper(), None):
            os.environ[key.upper()] = str(value)

    from src.web.serverconfig.FlaskConfig import FlaskConfig
    # Must be here to initiate the env variables before initialize
    # all components
    FlaskConfig()()