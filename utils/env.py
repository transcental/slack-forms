from dotenv import load_dotenv

from utils.prisma import DBClient

import os

load_dotenv()

class Env:
    def __init__(self):
        self.slack_bot_token = os.getenv("SLACK_BOT_TOKEN")
        self.slack_signing_secret = os.getenv("SLACK_SIGNING_SECRET")
        self.log_channel = os.getenv("LOG_CHANNEL")
        self.database_url = os.getenv("DATABASE_URL")

        self.port = int(os.getenv("PORT", 3000))

        if not self.slack_bot_token:
            raise ValueError("SLACK_BOT_TOKEN is not set")
        if not self.slack_signing_secret:
            raise ValueError("SLACK_SIGNING_SECRET is not set")
        if not self.log_channel:
            raise ValueError("LOG_CHANNEL is not set")
        if not self.database_url:
            raise ValueError("DATABASE_URL is not set")
        
        self.db = DBClient()

env = Env()
