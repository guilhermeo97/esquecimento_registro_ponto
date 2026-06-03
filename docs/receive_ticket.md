# Receive ticket function

## Métodos de requisição

```
HTTP Trigger -> POST
```

## Dados de entrada

Origem: dados que são recebidos da solicitação inicial de ajuste de ponto, contendo as informações básicas do ticket,
do funcionário, do tipo de ajuste solicitado, se é hora extra ou não, e os dados de aprovação do gerente (se for hora extra).

```python
time_adjustment_request = {
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

    # Required if is_overtime = True
    "manager_approval": {
        "manager_name": "Jose Silva",
        "evidence_url": "https://example.com/evidence/INC-1001"
    },

    "status": "RECEIVED",
    "created_at": "2026-05-20T10:00:00"
}
```

## Fluxo da função

- Receber requisição
- Body está vazio?
  - Se sim, retorna status code 400
- Body não seque a estrutura json solicitada?
  - Se sim, retorna status code 400
- O Body está is_overtime = True?
  - Se sim: "manager_approval" e "url_evidence" são válidos?
    - Enviar Body como mensagem para fila 'overtime-validation'
    - Retorna status code 203
- Enviar Body como mensagem para fila 'time-adjustment-requests'
- Retorna status code 203

## Saídas

### Sucesso

#### Quando há horas extras

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

#### Quando não há horas extras

```python
time_adjustment_requests = {
  "correlation_id": "abc123",
  "ticket_id": "INC-1001",
  "employee_id": "12345",
  "date": "2026-05-20",
  "adjustment_type": "entry",
  "requested_time": ["08:00"],
  "is_overtime": False,
  "status": "VALIDATED",
  "processed_at": "2026-05-20T10:00:00"
} # time-adjustment-requests
```

#### Resposta JSON

```python
{
	"message": "Request processed successfully"
}
```

### Falha

#### body vazio

```python
{
	"message": "Request body is empty"
}
```

#### body inválido

```python
{
    "message": "descricao erro..."
}
```
