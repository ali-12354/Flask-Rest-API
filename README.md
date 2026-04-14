# Flask-Rest-API
This project is a simple REST API built with Flask and SQLAlchemy for managing drinks in a local SQLite database.
It supports creating, listing, retrieving, and deleting drink records, making it a clean starter project for learning backend API development.
What it does
Stores drink data with a name and optional description
Persists data in SQLite
Returns JSON responses for all API routes
Automatically creates database tables on startup if they do not exist
Available endpoints
GET /
Basic health/welcome route
GET /drinks
Returns all drinks
GET /drinks/{id}
Returns one drink by ID
POST /drinks
Adds a new drink
DELETE /drinks/{id}
Deletes a drink by ID
If you want, I can also give you a full README template with setup steps, install commands, and example request/response payloads.
