
# GPTFilteredAnnouncementDM

This Yeager Workflow fetches announcements from specified channels and uses GPT
to filter relevant messages before sending them to a specified user through
direct messages. The workflow is composed of the following steps:
- Monitoring a list of channel IDs.
- Sending any detected messages in these channels to GPT for filtering.
- Delivering the filtered messages to a user's direct messages.

IOs - 
  - InputAnnouncementModel: A BaseModel with these fields:
      - channels_ids: List of channel IDs to monitor.
      - user_id: The ID of the user to send the filtered messages to.
      - gpt_key: The OpenAI API key needed for GPT access.
      - discord_bot_token: The Discord bot token to interact with the Discord API.

  - OutputDirectMessageModel: A BaseModel with these fields:
      - sent_messages: 
        A list of dictionaries containing:
          - channel: The ID of the announcement channel where the message was posted.
          - content: The original content of the filtered message.


## Initial generation prompt
description: "IOs - \"- InputAnnouncementModel: A BaseModel with these fields:\\n\
  \    - channels_ids: List\\\n  \\ of channel IDs to monitor.\\n    - user_id: The\
  \ ID of the user to send the filtered\\\n  \\ messages to.\\n    - gpt_key: The\
  \ OpenAI API key needed for GPT access.\\n    -\\\n  \\ discord_bot_token: The Discord\
  \ bot token to interact with the Discord API.\\n\\n\\\n  - OutputDirectMessageModel:\
  \ A BaseModel with these fields:\\n    - sent_messages:\\\n  \\ A list of dictionaries\
  \ containing:\\n        - channel: The ID of the announcement\\\n  \\ channel where\
  \ the message was posted.\\n        - content: The original content\\\n  \\ of the\
  \ filtered message.\\n\"\n"
name: GPTFilteredAnnouncementDM


## Transformer breakdown
- Monitor specified channel IDs for new messages.
- Send gathered messages to GPT for filtering.
- Send filtered messages to user's direct messages.

## Parameters
[]

        