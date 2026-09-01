from pathlib import Path
import shutil
from src.models.project import Project
from src.helpers.config import Settings, get_settings


class ProjectService:

    def get_or_create_project(self,project_id: int) -> Project:

        settings=get_settings()
        path = Path(settings.DATA_PATH) / str(project_id)

        if path.exists():
            
            return Project(project_id=project_id,path=str(path))

        
        path.mkdir(parents=True, exist_ok=True)
        return Project(project_id=project_id,path=str(path))

    def get_project(self, project_id: int) -> Project | None:

        settings = get_settings()
        path = Path(settings.DATA_PATH) / str(project_id)

        if not path.exists():
            return None

        return Project(
            project_id=project_id,
            path=str(path)
        )    

    

    def delete_project(self,project_id: int) ->bool:
        settings=get_settings()
        path = Path(settings.DATA_PATH) / str(project_id)
        if path.exists():
            shutil.rmtree(str(path))
            return True

        return False    
            

          
