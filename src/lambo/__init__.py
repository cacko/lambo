from corelog import register
from corelog import Handlers
import os


register(os.environ.get("LAMBO_LOG_LEVEL", "INFO"), Handlers.RICH)

