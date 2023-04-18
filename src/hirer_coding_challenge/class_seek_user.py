
from .class_user_job import UserJob
from typing import List, Union, Optional
from dataclasses import dataclass
from pyspark import Row
from datetime import date
from typing import List
import json

@dataclass
class User:
    """ Represents the seek user
    """

    first_name: str
    last_name: str
    job_history: List[UserJob]
    current_job: UserJob
    current_job_date: None

    def __init__(self, input_data: Union[dict, Row]):
        if isinstance(input_data, Row):
            data = input_data.asDict(recursive=True)
        elif isinstance(input_data, dict):
            print(input_data)
            data = input_data
        else:
            print(input_data)
            return
        self.first_name = data.get('firstName')
        self.last_name = data.get('lastName')
        job_history = []
        for user_job_data in data["jobHistory"]:
            user_job = UserJob(
                location=user_job_data["location"],
                salary=user_job_data["salary"],
                title=user_job_data["title"],
                from_date=date.fromisoformat(user_job_data["fromDate"]),
                to_date=user_job_data["toDate"],
            )
            if user_job_data["toDate"] is None:
                self.current_job = user_job_data
                self.current_job_date = date.fromisoformat(user_job_data["fromDate"])
            job_history.append(user_job)
        self.job_history = job_history

    def get_average_salary(self) -> Optional[float]:
        if hasattr(self, "job_history"):
            user_job_count = len(self.job_history)
            if user_job_count > 0:
                return sum(user_job.salary for user_job in self.job_history)/user_job_count
            else:
                return None
        else:
            return None

    def get_current_salary(self) -> Optional[int]:
        if hasattr(self, "current_job"): 
            if self.current_job is not None:
                return self.current_job["salary"]
            else:
                print(self)
        return None

    def get_current_from_date(self) -> Optional[date]:
        if hasattr(self, "current_job_date"):    
            return self.current_job_date
        return None
    
    def get_current_job(self) -> Optional[UserJob]:
         if hasattr(self, "current_job"): 
            if self.current_job is not None:
                return self.current_job
    
    def is_currently_working(self) -> Optional[bool]:
        return bool(self.get_current_job())    

    def get_highest_paying_job(self) -> Optional[UserJob]:
        if not self.job_history:
            return None
        
        sorted_jobs = sorted(self.job_history, key=lambda x: x.salary, reverse=True)

        return sorted_jobs[0]