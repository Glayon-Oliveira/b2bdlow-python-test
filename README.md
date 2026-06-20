# Desafio Técnico - Estágio Python da b2bflow

## Descrição

Aplicação Python que consome uma lista de contatos cadastrados no Supabase e envia mensagens por meio da API da Z-API, limitando aos três primeiros contatos encontrados.

## Tecnologias

- Python
- Supabase
- Z-API

## Tabela `contatos` no Supabase

| Campo |
|--------|
| id |
| name |
| phone |

## Configuração

Forneça as variáveis de ambiente por meio do arquivo `.env` ou no próprio ambiente de execução.

Variáveis necessárias:

### Variáveis para o Supabase
- `SUPABASE_URL` - URL do projeto Supabase
- `SUPABASE_KEY` - Chave de acesso


### Variáveis para o Z-API

- `ZAPI_INSTANCE` - ID da instância da Z-API
- `ZAPI_INSTANCE_TOKEN` - Token da instância da Z-API
- `ZAPI_API_KEY` - Chave de segurança da Z-API

Elas também são descritas em `.env.example`.

## Dependências

Instale as dependências:

```bash
pip install -r requirements.txt
```

Nota: Recomenda-se criar um ambiente virtual

## Execução

Para executar use:

```bash
python main.py
```

## Mensagem enviada

```text
Olá, <nome_contato> tudo bem com você?
```


## Funcionamento

- Busca os contatos cadastrados no Supabase
- Limita os contatos aos três primeiros
- Monta uma mensagem personalizada com o nome do contato
- Envia as mensagens por meio da API da Z-API
- Exibe o resultado no terminal
