from fastapi import APIRouter, UploadFile, File, Path

from src.controllers.file_controller import FileController
from src.services.file_service import FileService
from src.helpers.config import get_settings

router = APIRouter(prefix="/files", tags=["Files"])

file_service = FileService(config=get_settings())
file_controller = FileController(file_service=file_service)

@router.post("/upload/{project_id}")
async def upload_file(
    project_id: int = Path(..., gt=0),
    file: UploadFile = File(...)
):
    return await file_controller.upload_file(
        file=file,
        project_id=project_id
    )

@router.delete("/{project_id}/{file_id}")
def delete_file(project_id: int, file_id: str):
    return file_controller.delete_file(
        project_id=project_id,
        file_id=file_id
    )    