# Project 3 Overview – Movie Watchlist Client

For Project 3, I developed a web-based frontend client for the Movie Watchlist REST API created in Project 2. The objective of this project was to demonstrate two-way communication between a browser-based client and a FastAPI backend service using HTTP requests.

The frontend was built using HTML, CSS, and JavaScript, and it communicates with the backend using the Fetch API. The backend runs on port 8000 using Uvicorn, and the frontend is served separately on port 5500 to maintain proper client-server architecture.

The application successfully calls the following endpoints from Project 2:

Movies

    GET /movies (retrieve all movies)
    
    GET /movies/{movie_id} (retrieve a single movie)
    
    POST /movies (create a movie)
    
    PUT /movies/{movie_id} (update a movie)
    
    DELETE /movies/{movie_id} (delete a movie)

Lists

    GET /users/{user_id}/lists (retrieve lists for a user – subset)
    
    POST /users/{user_id}/lists (create a list)
    
    PUT /lists/{list_id} (update a list)
    
    DELETE /lists/{list_id} (delete a list)

This satisfies the requirement to call all GET methods (get all, get single, and get subset) and demonstrate full CRUD functionality.

During integration, I encountered issues including CORS restrictions between the frontend and backend servers, MySQL connection errors, and database integrity constraints when attempting to create duplicate records. These were resolved by configuring FastAPI CORSMiddleware, ensuring the MySQL server was running, and handling unique constraints properly.

ChatGPT was used to help generate the frontend structure and Fetch API calls. While it accelerated development, debugging and configuration required manual understanding of REST architecture and database connectivity.

The final system demonstrates successful client-server communication and full interaction with the database through the REST API. Screenshots included in the submission show all required operations functioning correctly.
## Tech Stack
- MySQL Community Server
- Python 3
- mysql-connector-python

## Project Features
- MySQL database with **5 tables** and proper primary/foreign key relationships
- SQL scripts to create the schema and insert **50+ rows** of test data
- Python data access layer (DAL) with CRUD operations
- Console-based application that retrieves and displays database records

## Repository Structure

##To run this application locally, the following software is required:

    - Python 3.10+
    
    - FastAPI
    
    - Uvicorn
    
    - MySQL Server
    
    - mysql-connector-python
    
    - A web browser


