Murilo Gomes Sardinha
RA: 2401763
João Manoel Lelis Oliveira
RA:2401807
Vinicius Janini
RA:2401580



# sistema_transportadora_api

Sistema de gestão com entidades: Moradores, Apartamentos, Funcionários, Contas e Admin.

## Como rodar
```bash
pip install -r requirements.txt
python app.py
```
Acesse: http://localhost:5000/docs

## Rotas (resumo)
- /moradores (CRUD)
- /apartamentos (CRUD)
- /funcionarios (CRUD)
- /contas (CRUD)
- /admin (criar/listar/remover)

Swagger é gerado a partir das docstrings e agrupado por entidade (primeiro segmento da rota).
