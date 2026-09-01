from pydantic import BaseModel, Field

class ProjectRequest(BaseModel):
    
    project_id:int=Field(...,gt=0)