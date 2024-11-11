from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from time import sleep, time
from queue import Queue
import inspect
import logging

client = None
log_queue = Queue()
log_channel = ""

def initialise_logger():
    global client, log_channel
    from utils.env import env
    client = WebClient(token=env.slack_bot_token)
    log_channel = env.log_channel
    logging.basicConfig(level=logging.INFO)

def process_logs():
    global log_channel
    while True:
        message = log_queue.get()
        try:
            client.chat_postMessage(channel=log_channel, text=message, username="Fillout Logger", icon_emoji=":robot_face:")
            logging.log(logging.INFO, message)
        except SlackApiError as e:
            if e.response["error"] == "ratelimited":
                retry_after = int(e.response.headers.get("Retry-After", 1))
                print(f"Rate limited, retrying in {retry_after} seconds.")
                logging.warning(f"Rate limited, retrying in {retry_after} seconds.")
                sleep(retry_after)
                log_queue.put(message)
            else:
                print(f"Failed to log message: {e.response['error']}")
                logging.error(f"Failed to log message: {e.response['error']}")
        sleep(0.1)
        log_queue.task_done()

def log_message(message: str):
    caller = inspect.stack()[1].function
    timestamp = int(time())
    message = f"""
Caller: {caller}
Message: ```{message}```
Time: <!date^{timestamp}^{{date_num}} {{time_secs}}|Fallback Text>
"""
    log_queue.put(message)
