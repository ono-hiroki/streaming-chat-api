# app/use_cases/project_request_model.py
from pydantic import BaseModel

class IndexProjectRequest(BaseModel):
    query: str = ""