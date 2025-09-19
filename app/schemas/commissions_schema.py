from pydantic import BaseModel, Field

class Commission(BaseModel):
    period_id: int
    member_id: int
    position_id: int
