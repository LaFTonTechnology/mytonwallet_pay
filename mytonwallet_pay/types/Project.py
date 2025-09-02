from pydantic import BaseModel


class Project(BaseModel):
    name: str
    projectId: int
    wallet: str
