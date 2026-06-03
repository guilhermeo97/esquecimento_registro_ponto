# Validate Overtime function

## Métodos de requisição

```
Queue Trigger
```

## Dados de entrada

Origem: Após identificar que o chamado recebido é uma hora extra.

```python
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
        "evidence_url": "https://example.com/evidence/INC-1001"
    },
    "status": "OVERTIME_ANALYSE",
    "processed_at": "2026-05-20T10:00:00"
} # overtime-validation
```

## Fluxo da função

- Uma nova mensagem entra na fila overtime-validation

## Saídas

### Sucesso

#### Quando há horas extras

```python

```

#### Quando não há horas extras

```python

```

#### Resposta JSON

```python

```

### Falha

#### body vazio

```python

```

#### body inválido

```python

```
