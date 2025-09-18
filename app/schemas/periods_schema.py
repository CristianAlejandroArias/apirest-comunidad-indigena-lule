from pydantic import BaseModel
from datetime import date

class Period(BaseModel):
    start_period: date
    end_period: date

