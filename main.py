import os
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Make sure to set this in your .env file

app = FastAPI()

# Serve the HTML frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI HTML Frontend</title>
        </head>
        <body>
            <h1>Welcome to the FastAPI Application</h1>
            <p><a href="/api/data">Get Data</a></p>
        </body>
    </html>
    '''

# Secure API endpoint
@app.get("/api/data")
async def get_data(api_key: str = Depends(lambda: API_KEY)):
    if api_key != API_KEY:
        return {"error": "Invalid API Key"}
    return {"message": "Access granted to secure data."}

# To run the app: uvicorn main:app --reload