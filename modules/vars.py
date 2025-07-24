import os

API_ID    = os.environ.get("API_ID", "289666784")
API_HASH  = os.environ.get("API_HASH", "a3f521a35694e90c52151873af3a7d2c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8337452130:AAFoz6ST_Jh5sDKPlMfiJOrnCfUfWhH48F0") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 6969))  # Default to 8000 if not set
