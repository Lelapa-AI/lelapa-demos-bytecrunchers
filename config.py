from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_TOKEN = os.getenv("TURN_API_TOKEN")
VULA_VULA = os.getenv("VULAVULA_TOKEN")