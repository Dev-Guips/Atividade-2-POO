
# Sistema de Locadora em Python

Este projeto implementa um **sistema de gerenciamento de locadora** usando Python e POO (Programação Orientada a Objetos).  
O sistema permite gerenciar filmes, usuários, empréstimos, devoluções e multas por atraso.

> Este projeto foi desenvolvido com base no algoritmo fornecido pelo professor **Edson de Oliveira Vieira**, da disciplina **Linguagem Orientada a Objetos** do **4º semestre de Ciência da Computação** da Faculdade Impacta.  
> 📧 Contato: **edson.vieira@faculdadeimpacta.com.br**
---
## Pré-requisitos

- Python 3.10+ instalado
- Recomenda-se criar um **ambiente virtual (venv)** para o projeto:

```bash
python -m venv venv
````

* Ativar o venv:

  * **Windows:** `venv\Scripts\activate`
  * **Linux/Mac:** `source venv/bin/activate`

* Instalar dependências:

```bash
pip install -r requirements.txt
```

> Atualmente, o projeto depende apenas do `pytest` para testes automatizados.

---

## Executando o Sistema

Para executar o exemplo interativo:

```bash
python main.py
```

Você poderá ver a simulação de empréstimos e devoluções de filmes, incluindo status e multas.

---

## Testes Automatizados

O projeto possui testes unitários com **pytest** para validar:

* Empréstimo e devolução de filmes
* Limite máximo de 3 empréstimos por usuário
* Tentativa de pegar filmes indisponíveis
* Devolução de filmes não emprestados
* Multas por atraso

### Rodando os testes

Recomenda-se usar o parâmetro `-s` para que o `pytest` mostre os `print()` do teste, incluindo o valor das multas:

```bash
pytest -s tests/test_locadora.py
```

---

## Exemplo de Saída de Teste de Multa

Para um filme devolvido com atraso de 5 dias:

```
Filme devolvido com multa de R$ 5.00
```

---

## Observações

* O limite de empréstimos por usuário é **3 filmes**.
* A multa por atraso é de **R$ 1,00 por dia** após 15 dias de empréstimo.
* Recomendamos não subir a pasta `venv` para o repositório. Utilize o `.gitignore`.

---

## Autores

* **Gabriel Muchon Pavanelli**
  📧 [gabriel.pavanelli@aluno.faculdadeimpacta.com.br](mailto:gabriel.pavanelli@aluno.faculdadeimpacta.com.br)

* **Guilherme Pinheiro Dos Santos**
  📧 [guilherme.psantos@aluno.faculdadeimpacta.com.br](mailto:guilherme.psantos@aluno.faculdadeimpacta.com.br)

> Desenvolvido com base no algoritmo do professor **Edson de Oliveira Vieira**
> 📧 [edson.vieira@faculdadeimpacta.com.br](mailto:edson.vieira@faculdadeimpacta.com.br)


