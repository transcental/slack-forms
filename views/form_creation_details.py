def get_modal() -> dict:
    return {
        "type": "modal",
        "callback_id": "create_form_details",
        "title": {
            "type": "plain_text",
            "text": "Create a Form",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Continue",
            "emoji": True
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "blocks": [
            {
                "type": "input",
                "block_id": "title",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "title",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Adopt a Dino"
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "Form Title",
                    "emoji": True
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_The title of the form. Will be shown to users_"
                    }
                ]
            },
            {
                "type": "input",
                "block_id": "description",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "description",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Adopt your very own dinosaur to take home and cuddle"
                    }
                },
                "label": {
                    "type": "plain_text",
                    "text": "Description",
                    "emoji": True
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "_This will be shown to people visiting your form. It should be short and explain what it is_"
                    }
                ]
            }
        ]
    }
