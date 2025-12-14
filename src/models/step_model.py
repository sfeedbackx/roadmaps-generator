from datetime import datetime
from typing import Optional, List
from step_skill_model import StepSkillBase, StepSkillUpdate


class StepBase(StepSkillBase):
    roadmap_id: str
    step_number: int


class StepCreate(StepBase):
    pass


class StepUpdate(StepSkillUpdate):
    step_number: Optional[int] = None
    prerequisites: Optional[List[str]] = None


class Step(StepBase):
    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
