# 🚀 Building REST APIs with FastAPI

## 🎯 Objective

Build a production-ready REST API using the FastAPI framework. You'll learn how to create endpoints, handle HTTP methods, validate data with Pydantic models, and implement error handling. This assignment covers API design principles and best practices for modern web development.

## 📝 Tasks

### 🛠️ Task 1: Create Basic Endpoints

#### Description
Set up a FastAPI application with basic GET and POST endpoints. Create a simple in-memory data store to manage a collection of items.

#### Requirements
Completed program should:

- Initialize a FastAPI application with proper imports
- Implement a GET endpoint that returns all items as a list
- Implement a GET endpoint that retrieves a single item by ID
- Implement a POST endpoint that accepts JSON data and adds a new item
- Define Pydantic models for request/response validation

### 🛠️ Task 2: Add CRUD Operations

#### Description
Extend the API with full CRUD (Create, Read, Update, Delete) functionality. Implement proper HTTP status codes and error handling for edge cases.

#### Requirements
Completed program should:

- Implement a PUT endpoint to update an existing item
- Implement a DELETE endpoint to remove an item
- Return appropriate HTTP status codes (200, 201, 404, 400)
- Raise HTTPException for invalid requests or missing resources
- Validate that item IDs exist before operations

### 🛠️ Task 3: Add Data Validation & Query Parameters

#### Description
Enhance the API with input validation and query parameter filtering. Users should be able to filter and search the data.

#### Requirements
Completed program should:

- Use Pydantic models with field validation (type hints, constraints)
- Add query parameters for filtering results (e.g., search by name)
- Implement optional query parameters with default values
- Validate pagination parameters (skip, limit) if applicable
- Return meaningful error messages for validation failures

### 🛠️ Task 4: Document & Test the API (Stretch Goal)

#### Description
Generate automatic API documentation and write basic tests to ensure endpoints work correctly.

#### Requirements
Completed program should:

- Use FastAPI's automatic interactive documentation (Swagger UI, ReDoc)
- Add docstrings to all endpoints
- Write unit tests for at least 2-3 key endpoints
- Test both successful and error scenarios
- Verify response validation and status codes
