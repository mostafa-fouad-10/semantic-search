from fastapi import UploadFile
from src.helpers.config import Settings
from src.models.enums import ResponseSignal
from pathlib import Path
from src.helpers.id_generator import generate_id
from src.models.file import File
from src.services.project_service import ProjectService
import shutil

class FileService:

    FILE_ALLOWED_TYPES = {
        "application/pdf",
        "text/plain",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    }

    def __init__(self, config: Settings):
        self.config = config

    async def validate_uploaded_file(self, file: UploadFile):

        if file.content_type not in self.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size is not None and file.size > self.config.MAX_FILE_SIZE:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value

    async def save_file(self, file: UploadFile, project_id: int):

        project = ProjectService().get_or_create_project(project_id)

        file_id = generate_id()

        file_dir = Path(project.path) / file_id
        file_dir.mkdir(parents=True, exist_ok=True)

        file_path = file_dir / file.filename

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return File(
            file_id=file_id,
            file_name=file.filename,
            project_id=project_id,
            path=str(file_path)
        )

    def delete_file(self, project_id: int, file_id: str) -> bool:

        project = ProjectService().get_project(project_id)

        if project is None:
            return False

        file_dir = Path(project.path) / file_id

        if not file_dir.exists():
            return False

        shutil.rmtree(file_dir)

        return True





