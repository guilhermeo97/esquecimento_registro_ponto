# Automação de esquecimento de registro em sistema de Ponto Eletrônico

## Visão Geral

Este projeto tem como objetivo automatizar o processo de ajustes de ponto corporativo utilizando uma arquitetura orientada a eventos baseada em Azure Functions.

O cenário foi inspirado em um processo real de negócio envolvendo abertura de chamados para correção de registros de ponto em um sistema terceiro.

Atualmente, o processo é altamente manual e depende da atuação humana em múltiplas etapas, incluindo:

- validação de regras de negócio
- verificação de inconsistências de ponto
- consulta de acessos físicos
- análise de aprovações de gestores
- ajustes manuais no sistema
- encerramento de chamados

A proposta deste projeto é modelar uma arquitetura moderna, desacoplada e resiliente utilizando serviços serverless da Azure para automatizar parte significativa desse fluxo.

## Fluxo Geral da Automação

O fluxo modelado até o momento segue a seguinte estrutura:

```
Sistema de Chamados
        ↓
Azure Function HTTP
        ↓
Fila de processamento
        ↓
Validação de hora extra
        ↓
Análise de registros no sistema de ponto eletrônico
        ↓
Consulta de evidências de acesso
        ↓
Aplicação do ajuste
        ↓
Persistência do workflow
        ↓
Callback para sistema de chamados
```
