from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL  =os.getenv("WEBHOOK_URL")

RELOAD: bool = os.getenv("RELOAD", "true").lower() in {"1", "true", "yes"}
DROP_PENDING: bool = os.getenv("DROP_PENDING", "false").lower() in {"1", "true", "yes"}

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = BASE_DIR / "templates"