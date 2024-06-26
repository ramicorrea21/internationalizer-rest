#### **Code Internationalizer Backend 🌍**

This repository contains the backend application for the Code Internationalizer, designed to support the frontend by processing code translations using OpenAI's API. It's built using Flask, a lightweight and powerful web framework that ensures efficient handling of requests with ease of scalability.

### **NOTE: This repo includes the Flask API. You can find the frontend application in the repo: [Frontend Repository](https://github.com/ramicorrea21/code-internationalizer)**

#### **⚒️STACK**:
- [OPENAI API](https://openai.com/blog/openai-api) for leveraging advanced AI to translate code comments and strings.
- [Flask](https://flask.palletsprojects.com/) as the lightweight WSGI web application framework to serve the API.
- [Python](https://www.python.org/) for backend scripting, providing a powerful yet easy-to-use language for web services.
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) for handling Cross-Origin Resource Sharing (CORS), allowing the frontend to interact securely with the backend.
- [Gunicorn](https://gunicorn.org/) as a Python WSGI HTTP Server for UNIX, serving Flask applications in a production environment.
- [PostgreSQL](https://www.postgresql.org/) for database services, if the application requires any form of data persistence.

#### **Setup and Installation**

1. **Clone the Repository**
   ```
   git https://github.com/ramicorrea21/internationalizer-rest.git
   cd internationalizer-rest
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**
   - Create a `.env` file in the root directory and set the following variables:
     ```
     OPENAI_API_KEY='your_openai_api_key_here'
     ```

4. **Run the Server**
   ```
   flask run
   ```
   This command starts the Flask server. The API will be available at `http://localhost:5000`.

#### **API Endpoints**

- `POST /translate`: Receives source code and language details, returns the translated code.

#### **Error Handling**

- Proper error messages are returned in JSON format for any failed API requests.

#### **Running with Gunicorn**

For production environments, it's recommended to use Gunicorn as the WSGI server:
```
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app()"
```
This command will start the server with 4 worker processes.

#### **Dependencies**

- Detailed list of all project dependencies included in the `requirements.txt` file, ensuring easy setup.

This README file provides a comprehensive overview to help developers understand and set up the backend for the Code Internationalizer effectively.
