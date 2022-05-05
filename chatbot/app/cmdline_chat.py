import asyncio
import uuid
from rasa.core import constants
from rasa.core.channels import console

asyncio.run(console.record_messages(
    server_url = constants.DEFAULT_SERVER_FORMAT.format("http", 5005),
        sender_id = uuid.uuid4().hex,
))

