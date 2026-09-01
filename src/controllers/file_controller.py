from fastapi import UploadFile
from src.services.file_service import FileService


class FileController:

    def __init__(self, file_service: FileService):
        self.file_service = file_service

    async def upload_file(self, file: UploadFile, project_id: int):

        is_valid, message = await self.file_service.validate_uploaded_file(file)

        if not is_valid:
            return {
                "success": False,
                "message": message
            }

        saved_file = await self.file_service.save_file(
            file=file,
            project_id=project_id
        )

        return {
            "success": True,
            "message": "File uploaded successfully",
            "file": saved_file.model_dump()
        }

    def delete_file(self, project_id: int, file_id: str):

        deleted = self.file_service.delete_file(
            project_id=project_id,
            file_id=file_id
        )

        if not deleted:
            return {
                "success": False,
                "message": "File not found"
            }

        return {
            "success": True,
            "message": "File deleted successfully"
        }