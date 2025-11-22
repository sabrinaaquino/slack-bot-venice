from typing import Optional, List
from slack_sdk.web.slack_response import SlackResponse
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

"""
Parses a conversation history, excluding messages from the bot,
and formats it as a string with user IDs and their messages.
Used in `app_mentioned_callback`, `dm_sent_callback`,
and `handle_summary_function_callback`."""


def parse_conversation(conversation: SlackResponse) -> Optional[List[dict]]:
    parsed = []
    try:
        for message in conversation:
            # Skip messages without text content (file uploads, reactions, etc.)
            if not message.get("text"):
                continue
            
            # Get user or bot_id
            user = message.get("user")
            bot_id = message.get("bot_id")
            
            # Skip if neither user nor bot_id exists
            if not user and not bot_id:
                continue
            
            text = message["text"]
            msg_dict = {"text": text}
            
            if user:
                msg_dict["user"] = user
            if bot_id:
                msg_dict["bot_id"] = bot_id
                
            parsed.append(msg_dict)
        return parsed
    except Exception as e:
        logger.error(e)
        return None
