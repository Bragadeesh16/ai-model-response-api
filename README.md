# Project Name: Ai-model-response-api

## 1. How to Run the Project

### Prerequisites
Ensure the following are installed on your system:

- Python 3.10+
- Django
- SQLAlchemy (or any other database of your choice)
- SQLite (or another database, if preferred)
- Redis (for background tasks with Celery)
- pytest (for testing)
- Python `dotenv` (for loading environment variables)

### Installation Steps

1. **Create a new folder and navigate to it**:

    ```bash
    mkdir ai-model-response-api
    cd ai-model-response-api
    ```

2. **Set up a virtual environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate  # For Linux/MacOS
    env\Scripts\activate     # For Windows
    ```

3. **Clone the repository**:

    ```bash
    git clone https://github.com/Bragadeesh16/ai-model-response-api
    cd ai-model-response-api
    ```

4. **Install the required dependencies**:

    ```bash
    pip install -r pip-requirements.txt
    ```

5. **Run database migrations** (if you're using Django's default database setup with SQLite or any other database):

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Django development server**:

    ```bash
    python manage.py runserver
    ```

   The application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

7. **Setup the `.env` File**:

    1. Create a `.env` file in the root directory of the project.
   
    2. Add your Gemini API key to the `.env` file:
    
        ```env
        GEMINI_API_KEY=your-gemini-api-key-here
        ```

    3. Make sure to **never share** your `.env` file or commit it to version control.
    
    4. To load the environment variables from the `.env` file, install the `python-dotenv` package:

        ```bash
        pip install python-dotenv
        ```

    5. Your `.env` file will be automatically loaded in the project when you use `os.getenv("GEMINI_API_KEY")` in your code.

8. **Start Redis**:

    Open a new terminal and run the following to start Redis:

    ```bash
    redis-server
    ```

    If you encounter an error like "port is already in use," follow these steps to resolve it:

    1. **Check if Redis is already running**:

        ```bash
        ps aux | grep redis
        ```

    2. **Stop the Redis server**:

        ```bash
        redis-server --shutdown
        ```

        Or, you can kill the process manually:

        ```bash
        sudo kill <PID>
        ```

    3. **Free the port** if it's still in use:

        ```bash
        sudo lsof -i :6379
        sudo kill <PID>
        ```

    4. **Restart Redis**:

        ```bash
        redis-server
        ```

9. **Start Celery** in the same terminal where Redis is running:

    In the same terminal where you ran `redis-server`, execute:

    ```bash
    celery -A your_project_name worker --loglevel=info
    ```

10. **Open a new terminal and run pytest** to ensure tests pass:

    ```bash
    pytest
    ```

## 2. Postman Collection

A Postman collection is included in this repository to help you test the API endpoints.

### How to Use the Postman Collection

1. Download the Postman collection from the `postman` folder in the repository:

    [Download the Postman Collection](./postman/ai-model-response-api-collection.json)

2. Import the collection into Postman:
    - Open Postman.
    - Click on the **Import** button (top-left).
    - Choose the **File** option and select the `ai-model-response-api-collection.json` file.

3. Once imported, you can use the collection to interact with the API endpoints.
