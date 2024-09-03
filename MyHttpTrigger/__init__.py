import azure.functions as func
from fastapi import FastAPI, Response
from azure.functions import AsgiMiddleware

# Initialize the FastAPI app
fast_app = FastAPI()

@fast_app.get("/MyHttpTrigger")
async def my_http_trigger():
    return Response(content="Hello from FastAPI at MyHttpTrigger", media_type="text/plain")

# Define the main function as the entry point for Azure Functions
async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    # Use AsgiMiddleware to handle the FastAPI app asynchronously
    return await AsgiMiddleware(fast_app).handle_async(req, context)
