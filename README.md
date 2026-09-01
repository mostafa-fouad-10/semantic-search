# Semantic Search API

A FastAPI-based backend for managing projects and uploaded documents as part of a semantic search system.

## What I Implemented

### File Management

Implemented the initial file management layer for the semantic search system:

* Create or retrieve a project using a `project_id`.
* Upload files to a project.
* Validate uploaded files before saving.
* Validate supported file types.
* Validate maximum file size.
* Generate a unique `file_id` for every uploaded file.
* Store each file inside its project directory.
* Delete uploaded files.
* Return structured API responses.

### Supported File Types

The API currently supports:

* PDF
* TXT
* DOCX

### Storage Structure

Uploaded files are organized by project and file ID:

```text
data/uploads/
└── {project_id}/
    └── {file_id}/
        └── original_filename
```


## Architecture

The backend follows a simple layered architecture:

```text
Route
  ↓
Controller
  ↓
Service
  ↓
Project Service
```

### Routes

Responsible for defining HTTP endpoints and handling request parameters.

### Controllers

Responsible for coordinating the request flow between routes and services.

### Services

Contain the main business logic, such as:

* File validation
* File saving
* File deletion
* Project creation/retrieval

### Models

Define the structure of domain objects such as:

* Project
* File

### Schemas

Define and validate API request data.

## API Endpoints

### Upload File

```http
POST /files/upload/{project_id}
```

Uploads a file to the specified project.

### Delete File

```http
DELETE /files/delete/{project_id}/{file_id}
```

Deletes a file from the specified project.




