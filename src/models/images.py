from typing import List

from pydantic import BaseModel, Field


class ImagesModel(BaseModel):
    _id: str = Field(alias='_id')
    file_id: str
    depth: float
    pixels: List[int]
    color: str



class StateModel:
    _id: str = Field(alias='_id')
    state_abs: str
    state_net_revenue_generation: float


class PlantsModel:
    _id: str = Field(alias='_id')
    plant_name: str
    state_abs: str
    plant_net_revenue_generation: float
