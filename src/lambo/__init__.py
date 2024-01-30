from corelog import register
from corelog import Handlers
import os

__name__ = "lambo"

register(os.environ.get("LAMBO_LOG_LEVEL", "INFO"), Handlers.RICH)

