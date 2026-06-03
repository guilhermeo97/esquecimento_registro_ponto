import logging

import azure.functions as func
from jsonschema import ValidationError

from esquecimento_registro.json_schema import validate_body_json_schema as validate_body

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="receive_ticket", methods=["POST"])
def receive_ticket(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        ticket_data = req.get_json()
        validate_body(ticket_data)
        logging.info(f"Received ticket data: {ticket_data}")
        return func.HttpResponse("Ticket received successfully.", status_code=203)
    except ValidationError as e:
        logging.error(f"Invalid ticket data: {e}")
        return func.HttpResponse("Invalid ticket data.", status_code=400)
    except ValueError as e:
        logging.error(f"Error processing ticket data: {e}")
        return func.HttpResponse("Failed to process ticket data.", status_code=400)