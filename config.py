from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
API_TOKEN = os.getenv("API_TOKEN")