from prisma import Prisma
from utils.logger import log_message

class DBClient:
    def __init__(self):
        self.db = Prisma()
        self.db.connect()


    def create_user(self, user_id: str, email: str):
        try:
            log_message(f"Creating user {user_id} with email {email}")
            return self.db.user.upsert(
                where={
                    "id": user_id
                },
                data={
                    "create": {
                        "id": user_id,
                        "email": email
                    },
                    "update": {
                        "email": email
                    }
                }
            )
        except Exception as e:
            log_message(f"Error creating user {user_id}: {e}")


    def get_user(self, user_id: str):
        return self.db.user.find_unique({
            "where": {
                "id": user_id
            }
        })
    

    def create_form(self, title: str, description: str, user_id: str, email: str):
        try:
            log_message(f"Creating form \"{title}\" with description \"{description}\"")
            user = self.create_user(user_id, email)
            if not user:
                log_message(f"User {user_id} does not exist and could not be created. Cancelling form creation.")
                return
            else:
                log_message(f"User {user_id} exists.\nUser: {user}")
            form = self.db.form.create({
                "title": title,
                "description": description,
                "owners": {
                    "connect": {
                        "id": user_id
                    }
                },
                "userId": user_id
            })
            log_message(f"Form created: {form}")
        except Exception as e:
            log_message(f"Error creating form {title}: {e}")


    def get_forms(self, user_id: str):
        return self.db.form.find_many({
            "where": {
                "owners": {
                    "some": {
                        "id": user_id
                    }
                }
            }
        })
    

    def get_form(self, form_id: str):
        return self.db.form.find_unique({
            "where": {
                "id": form_id
            }
        })
