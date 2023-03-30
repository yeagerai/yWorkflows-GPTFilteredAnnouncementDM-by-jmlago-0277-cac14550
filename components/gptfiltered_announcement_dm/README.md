markdown
# Component Name

GPTFilteredAnnouncementDM

# Description

GPTFilteredAnnouncementDM is a Yeager Workflow component that processes announcements and sends direct messages (DMs) to a list of channels in a filtered manner. The component uses the provided GPT_KEY for filtering and the DISCORD_BOT_TOKEN to authenticate and send the messages through Discord.

# Input and Output Models

- **InputAnnouncementModel**: This model defines the input data for the component, containing:
    - channels_ids: A list of integer channel IDs that the DMs will be sent to.
    - user_id: An integer representing the user ID.
    - gpt_key: A string containing the GPT key.
    - discord_bot_token: A string containing the Discord bot token.

- **OutputDirectMessageModel**: This model defines the output data for the component, containing:
    - sent_messages: A list of dictionaries with keys "channel_id" (integer) and "message" (string), representing the messages sent to each channel.

# Parameters

- **args**: An instance of the InputAnnouncementModel, containing input data required by the component.
- **callbacks**: A parameter used to provide any additional callbacks (defaults to `None`). The default value `None` is used in the `transform()` method.

# Transform Function

The `transform()` method is an asynchronous function that processes and filters the input data, and then sends DMs to the specified channels:

1. Call the parent (AbstractWorkflow) `transform()` method, passing in the same `args` and `callbacks`.
2. Retrieve the `results_dict` from the parent transform() method, containing the "sent_messages" key.
3. Build the output using the OutputDirectMessageModel, and set the "sent_messages" value.
4. Return the output.

# External Dependencies

- FastAPI: A web framework for building APIs.
- Pydantic: A data validation and serialization library.
- Parent class "AbstractWorkflow": The base class for Yeager Workflow components.

# API Calls

No external API calls are made by this component.

# Error Handling

This component does not include any specific error handling logic. Errors occurring during processing will be propagated up to the parent class (AbstractWorkflow).

# Examples

To use the GPTFilteredAnnouncementDM component within a Yeager Workflow, follow these steps:

1. Create an instance of the InputAnnouncementModel with the expected input data:

