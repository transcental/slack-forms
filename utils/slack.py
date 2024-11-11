from slack_bolt import App
from slack_sdk import WebClient

from utils.env import env
from views.form_creation_details import get_modal as get_form_creation_details_modal

from typing import Callable, Any
from slack_sdk.models.views import View

app = App(
    token=env.slack_bot_token,
    signing_secret=env.slack_signing_secret
)

@app.command("/create-form") 
def create_form(ack: Callable, body: dict[str, Any], client: WebClient):
    ack()
    view = get_form_creation_details_modal()
    client.views_open(view=view, trigger_id=body["trigger_id"])


@app.view("create_form_details")
def create_form_details(ack: Callable, body: dict[str, Any], client: WebClient):
    ack()
    values = body["view"]["state"]["values"]
    title = values["title"]["title"]["value"]
    description = values["description"]["description"]["value"]
    text = f"""
Form title: {title}
Description: {description}
User: <@{body['user']['id']}>
"""
    client.chat_postMessage(channel=env.log_channel, text=text)
    user_id = body["user"]["id"]
    user_data = client.users_info(user=user_id)
    email = user_data["user"]["profile"]["email"]
    env.db.create_form(title, description, user_id, email)