# NotasAPP

Este é um projeto de gerenciamento de mensagens com suporte a Docker para facilitar o desenvolvimento e a implantação.

## 🙋‍♂️ Autores

Desenvolvido por João Antonio dos Santos Ilario.


## Estrutura do Projeto

- **backend/**: Contém a API do backend escrita em Python.
  - `app.py`: Ponto de entrada da aplicação backend.

## Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados.
- Python 3.11 (para desenvolvimento do backend).

## Funcionalidades

- Criação de notas
- Listagem de todas as anotações
- Interface responsiva feita com React
- Sincronização entre containers

## Tecnologias Utilizadas

- Backend: Python com FastAPI.
- Containerização: Docker.

## Como Executar

### Usando Docker

1. Certifique-se de que o Docker e o Docker Compose estão instalados.
2. No diretório raiz do projeto, execute:
   ```bash
   docker-compose up --build
   ```
3. Acesse o frontend em http://localhost e a API em http://localhost/api/

### Rodando a Imagem e os Conteiners

```bash
    docker-compose up --build
```