import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Hardcoded variables with your values
API_ID = "20787644"
API_HASH = "9dada820698e8a5fdd5e6cc78fac8567"
BOT_TOKEN = "7939164806:AAFM_IcYWxPqVVbKGbdlEThnXLQ4qHS1AYA"
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()  # Optional, for stats if needed
MUST_JOIN = "https://t.me/coding"

# Check if mandatory environment variables are set
if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")

# Convert API_ID to integer and handle any conversion errors
try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

# Adjust DATABASE_URL if using a PostgreSQL URL
if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")

# Now you can use these variables (API_ID, API_HASH, BOT_TOKEN, DATABASE_URL, MUST_JOIN) in your main bot script
