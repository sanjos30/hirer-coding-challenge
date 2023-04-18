from datetime import date
from typing import Optional
from dataclasses import dataclass

@dataclass
class UserJob:
    """ represents job of a seek user
    """
    
    title: str
    location: str
    salary: int
    from_date: date
    to_date: Optional[date]