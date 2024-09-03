import azure.functions as func
from flask import Flask, Response

# Initialize the Flask app
flask_app = Flask(__name__)

# Define a simple route
@flask_app.route('/MyHttpTrigger', methods=['GET'])
def return_http():
    return Response("<h1>Hello World™</h1>", mimetype="text/html")

# The entry point for Azure Functions
def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.WsgiMiddleware(flask_app.wsgi_app).handle(req)
