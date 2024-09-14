from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    LOGGER = True

   _ID = int(getenv("API_ID", 6))    
    API_HASH = getenv("API_HASH")
    DEEP_API = getenv("DEEP_API")
    ARQ_API_KEY = getenv("ARQ_API_KEY", "TBPYLF-SIOYFX-JALTSV-QEAMXE-ARQ")
    SPAMWATCH_API = getenv("SPAMWATCH_API", "t9HHtrsmy7faPQWloX8xCvdZK~puDP2RnHLpb~qijQqDj94mhcMQdDP_xO0a_Iwe")
    TOKEN = getenv("TOKEN")
    OWNER_ID = int(getenv("OWNER_ID", 1679112664
    OWNER_USERNAME = getenv("OWNER_USERNAME", "OfficialDurgesh")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "DNS_NETWORK")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002243074516
    MONGO_URI = getenv("MONGO_DB_URI")
    DB_NAME = getenv("DB_NAME", "AvaRobot")
    REDIS_URL = getenv("REDIS_URL", "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redisl.com:10186/default")
    DATABASE_URL = getenv("DATABASE_URL")

    # Check if DATABASE_URL is set and adjust if needed
    if DATABASE_URL:
        if DATABASE_URL.startswith("gres://"):
            DATABASE_URL = DATABASE_.replace("postgres://", "postgresql://", 1)
    else:
        raise ValueError("DATABASE_URL environment variable is not set")

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
