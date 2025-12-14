from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from step_model import Step


class RoadmapBase(BaseModel):
    user_id: str
    topic: str


class RoadmapCreate(RoadmapBase):
    pass


class RoadmapUpdate(BaseModel):
    topic: Optional[str] = None


class Roadmap(RoadmapBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class RoadmapWithSteps(Roadmap):
    steps: List[Step] = []

    class Config:
        from_attributes = True
