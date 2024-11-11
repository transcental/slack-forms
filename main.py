from utils.env import env
from utils.slack import app
from utils.logger import process_logs, initialise_logger, log_message
from threading import Thread
import sys
import traceback

def main():
    try:
        initialise_logger()
        Thread(target=process_logs, daemon=True).start()
        app.start(port=env.port)
    except Exception as e:
        log_message(f"Error: {e}")
        traceback.print_exc()



def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    log_message(f"Uncaught exception: {exc_value}")
    traceback.print_exception(exc_type, exc_value, exc_traceback)


if __name__ == "__main__":
    sys.excepthook = handle_exception
    main()