from abc import ABC

from pydantic import BaseModel


class CustomBaseModel(ABC, BaseModel):

    def __getitem__(self, item):
        return getattr(self, item)
