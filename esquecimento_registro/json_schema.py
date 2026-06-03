from jsonschema import validate, ValidationError
from typing import Any

def validate_body_json_schema(body: dict[str, Any]) -> None:
    """Validates schema of the request body."""
    schema = {
    "type": "object",
    "properties": {
        "ticket_id": {"type": "string"},
        "employee_id": {"type": "string"},
        "date": {"type": "string", "format": "date"},
        "is_overtime": {"type": "boolean"},
        # "requested_records": {
        #     "type": "array",
        #     "items": {
        #         "type": "object",
        #         "properties": {
        #             "type": {"type": "string", "enum": ["entry", "exit", "both"]},
        #             "time": {"type": "array", "items": {"type": "string", "pattern": r"^\\d{2}:\\d{2}$"}}}
        #         },
        #         "required": ["type", "time"]
        #     }
        # },

        # "is_overtime": {"type": "boolean"},

        # # Required if is_overtime = True
        # "manager_approval": {
        #     "type": ["object", "null"],
        #     "properties": {
        #         "manager_name": {"type": "string"},
        #         "evidence_url": {"type": "string", "format": "uri"}
        #     },
        #     # Only required if is_overtime is true
        #     # This will be handled in code after schema validation
        # },

        "created_at": {"type": "string", "format": "date-time"}},
    "required": ["ticket_id", "employee_id", "date", "is_overtime", "created_at"]
    }


    validate(instance=body, schema=schema)