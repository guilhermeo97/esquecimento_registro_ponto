from jsonschema import ValidationError


def test_request_body_validation():
    from function_app import validate_body
    valid_data = {
        "ticket_id": "INC-1001",
        "employee_id": "12345",
        "date": "2026-05-20",
        "created_at": "2026-05-20T10:00:00",
        "is_overtime": True
    }
    try:
        validate_body(valid_data)
        assert True, "Validation should pass for valid data"
    except ValidationError as e:
        assert False, f"Validation failed for valid data: {e}"