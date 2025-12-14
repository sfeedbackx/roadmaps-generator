from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from enum import Enum


class TypeEnum(str, Enum):
    REQUIRED = "REQUIRED"
    RECOMMENDED = "RECOMMENDED"
    OPTIONAL = "OPTIONAL"


class StepSkillBase(BaseModel):
    title: str
    description: str
    technologies: List[str] = []
    duration_hours: float
    difficulty_level: float
    study_hours_per_day: int
    type: TypeEnum = TypeEnum.REQUIRED
    free_resources: Optional[Dict[str, Any]] = None
    paid_resources: Optional[Dict[str, Any]] = None


class StepSkillUpdate(BaseModel):
    title: Optional[str] = None
    duration_hours: Optional[float] = None
    difficulty_level: Optional[float] = None
    study_hours_per_day: Optional[int] = None
    description: Optional[str] = None
    type: Optional[TypeEnum] = None
    free_resources: Optional[Dict[str, Any]] = None
    paid_resources: Optional[Dict[str, Any]] = None
