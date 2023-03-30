
import typing
from typing import List, Dict, Union
from fastapi import FastAPI
from pydantic import BaseModel
from core.workflows.abstract_workflow import AbstractWorkflow

class InputAnnouncementModel(BaseModel):
    channels_ids: List[int]
    user_id: int
    gpt_key: str
    discord_bot_token: str

class OutputDirectMessageModel(BaseModel):
    sent_messages: List[Dict[str, Union[int, str]]]

class GPTFilteredAnnouncementDM(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: InputAnnouncementModel, callbacks: typing.Any
    ) -> OutputDirectMessageModel:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        sent_messages = results_dict["sent_messages"]
        out = OutputDirectMessageModel(sent_messages=sent_messages)
        return out

gpt_filtered_announcement_dm_app = FastAPI()

@gpt_filtered_announcement_dm_app.post("/transform/")
async def transform(
    args: InputAnnouncementModel,
) -> OutputDirectMessageModel:
    gpt_filtered_announcement_dm = GPTFilteredAnnouncementDM()
    return await gpt_filtered_announcement_dm.transform(args, callbacks=None)
