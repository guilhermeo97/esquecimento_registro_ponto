
access_evidence_analysis = {
  "correlation_id": "abc123",
  "ticket_id": "INC-1001",
  "employee_id": "12345",
  "date": "2026-05-20",
  "adjustment_type": "entry",
  "requested_time": ["08:00"],
  "is_overtime": False,
  "status": "inconsistent_found",
  "datetime_received": "2026-05-20T10:00:00",
} # access-evidence-analysis

time_adjustment_processing = {
  "correlation_id": "abc123",
  "ticket_id": "INC-1001",
  "employee_id": "12345",
  "date": "2026-05-20",
  "adjustment_type": "entry",
  "requested_time": ["08:00"],
  "time_found": ["08:05"],
  "is_overtime": False,
  "status": "access_confirmed",
  "datetime_received": "2026-05-20T10:00:00",
} # time-adjustment-processing

ticket_finalization = {
  "correlation_id": "abc123",
  "ticket_id": "INC-1001",
  "employee_id": "12345",
  "date": "2026-05-20",
  "adjustment_type": "entry",
  "requested_time": ["08:00"],
  "time_found": ["08:05"],
  "status": "adjustment_applied",
  "datetime_received": "2026-05-20T10:00:00",
} # ticket-finalization

human_review = {
  "correlation_id": "abc123",
  "ticket_id": "INC-1001",
  "employee_id": "12345",
  "status": "",
  "reviewer": "Maria Oliveira",
  "review_comments": "Evidence is inconclusive, further investigation needed.",
  "datetime_reviewed": "2026-05-21T14:30:00",
} # human-review


# Analisar o que está abaixo e verificar se se faz sentido

"""
Workflow Contracts - Time Adjustment Automation
"""

# ==========================================
# INITIAL REQUEST
# ==========================================

time_adjustment_request = {
    "correlation_id": "abc123",
    "ticket_id": "INC-1001",
    "employee_id": "12345",
    "date": "2026-05-20",

    "requested_records": [
        {
            "type": "entry",
            "time": "08:00"
        }
    ],

    "is_overtime": False,

    # Required if is_overtime = True
    "manager_approval": {
        "manager_name": "Jose Silva",
        "approval_date": "2026-05-20",
        "evidence_url": "https://example.com/evidence/INC-1001"
    },

    "status": "RECEIVED",
    "created_at": "2026-05-20T10:00:00"
}

# Queue:
# time-adjustment-requests


# ==========================================
# OVERTIME VALIDATION
# ==========================================

overtime_validation = {
    "correlation_id": "abc123",
    "ticket_id": "INC-1001",
    "employee_id": "12345",
    "date": "2026-05-20",

    "requested_records": [
        {
            "type": "entry",
            "time": "08:00"
        }
    ],

    "is_overtime": True,

    "manager_approval": {
        "manager_name": "Jose Silva",
        "approval_date": "2026-05-20",
        "evidence_url": "https://example.com/evidence/INC-1001"
    },

    "overtime_validation": {
        "approved": True,
        "validated_by": "document-analysis-service",
        "validated_at": "2026-05-20T10:05:00"
    },

    "status": "OVERTIME_APPROVED"
}

# Queue:
# overtime-validation


# ==========================================
# TIME RECORD ANALYSIS
# ==========================================

time_record_analysis = {
    "correlation_id": "abc123",
    "ticket_id": "INC-1001",
    "employee_id": "12345",
    "date": "2026-05-20",

    "requested_records": [
        {
            "type": "entry",
            "time": "08:00"
        }
    ],

    "pontosoft_records": [
        {
            "type": "entry",
            "time": "13:00"
        }
    ],

    "analysis_result": {
        "inconsistency_found": True,
        "reason": "ODD_NUMBER_OF_RECORDS"
    },

    "status": "TIME_INCONSISTENCY_FOUND",

    "processed_at": "2026-05-20T10:10:00"
}

# Queue:
# access-evidence-analysis


# ==========================================
# ACCESS EVIDENCE ANALYSIS
# ==========================================

access_evidence_analysis = {
    "correlation_id": "abc123",
    "ticket_id": "INC-1001",
    "employee_id": "12345",
    "date": "2026-05-20",

    "requested_records": [
        {
            "type": "entry",
            "time": "08:00"
        }
    ],

    "resolved_records": [
        {
            "source": "turnstile",
            "type": "entry",
            "time": "08:05"
        }
    ],

    "access_validation": {
        "access_found": True,
        "difference_in_minutes": 5,
        "within_allowed_window": True
    },

    "status": "ACCESS_CONFIRMED",

    "processed_at": "2026-05-20T10:15:00"
}

# Queue:
# time-adjustment-processing


# ==========================================
# APPLY TIME ADJUSTMENT
# ==========================================

time_adjustment_processing = {
    "correlation_id": "abc123",
    "ticket_id": "INC-1001",
    "employee_id": "12345",
    "date": "2026-05-20",

    "requested_records": [
        {
            "type": "entry",
            "time": "08:00"
        }
    ],

    "resolved_records": [
        {
            "source": "turnstile",
            "type": "entry",
            "time": "08:05"
        }
    ],

    "adjustment_result": {
        "adjustment_applied": True,
        "adjustment_reason_code": 1,
        "interval_regenerated": False
    },

    "status": "ADJUSTMENT_APPLIED",

    "processed_at": "2026-05-20T10:20:00"
}

# Queue:
# ticket-finalization


# ==========================================
# FINALIZATION
# ==========================================

ticket_finalization = {
    "correlation_id": "abc123",
    "ticket_id": "INC-1001",

    "finalization": {
        "ticket_updated": True,
        "ticket_closed": True,
        "closure_message": "Time adjustment successfully applied."
    },

    "status": "COMPLETED",

    "processed_at": "2026-05-20T10:25:00"
}

# Queue:
# completed-adjustments


# ==========================================
# HUMAN REVIEW
# ==========================================

human_review = {
    "correlation_id": "abc123",
    "ticket_id": "INC-1001",
    "employee_id": "12345",

    "status": "MANUAL_REVIEW_REQUIRED",

    "review_reason": "ACCESS_NOT_FOUND",

    "review_details": {
        "assigned_to": "Maria Oliveira",
        "comments": "Evidence is inconclusive, further investigation needed."
    },

    "processed_at": "2026-05-20T10:30:00"
}

# Queue:
# human-review


# ==========================================
# POSSIBLE STATUS VALUES
# ==========================================

STATUS_VALUES = [
    "RECEIVED",
    "VALIDATED",
    "OVERTIME_APPROVED",
    "TIME_INCONSISTENCY_FOUND",
    "ACCESS_CONFIRMED",
    "ADJUSTMENT_APPLIED",
    "COMPLETED",
    "MANUAL_REVIEW_REQUIRED",
    "REJECTED"
]


# ==========================================
# POSSIBLE REVIEW REASONS
# ==========================================

REVIEW_REASONS = [
    "INVALID_MANAGER_APPROVAL",
    "TIME_RECORD_NOT_INCONSISTENT",
    "ACCESS_NOT_FOUND",
    "ACCESS_TIME_WINDOW_EXCEEDED",
    "PONTOSOFT_UNAVAILABLE",
    "UNKNOWN_ERROR"
]

