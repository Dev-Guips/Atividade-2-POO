# 📚 Sistema de Biblioteca Simples

Um projeto em Python que simula o funcionamento de uma biblioteca, permitindo gerenciar livros, usuários e empréstimos. O sistema inclui tratamento de exceções, controle de disponibilidade e testes automatizados com **pytest**.

---

## 🧾 Sumário
- [Introdução](#introdução)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Funcionalidades](#funcionalidades)
- [Testes](#testes)
- [Dependências](#dependências)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## 🚀 Introdução

O **Sistema de Biblioteca Simples** foi desenvolvido para demonstrar conceitos de Programação Orientada a Objetos (POO), exceções personalizadas e testes automatizados em Python.  
Ele permite o cadastro de livros, o controle de empréstimos e devoluções, além do tratamento de erros, como tentativa de empréstimo de livro indisponível ou ultrapassagem do limite de livros emprestados.

---

## 📁 Estrutura do Projeto

```text
ap_exemplo/
├── src/
│   ├── biblioteca.py
│   └── test_biblioteca.py
├── venv/
├── main.py
├── requirements.txt
└── README.md
```




---

## ⚙️ Instalação

1. **Clone este repositório**
   ```bash
   git clone https://github.com/seu-usuario/ap_exemplo.git
   cd ap_exemplo

## Crie um ambiente virtual
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

## Instale as dependências
pip install -r requirements.txt


## Execute o sistema a partir do arquivo principal:
python main.py

## A saída esperada deve exibir um menu simples com a simulação do gerenciamento de uma biblioteca:
=== SISTEMA BIBLIOTECA SIMPLES ===

Livro emprestado com sucesso!
Erro: LivroIndisponivelError

## Para executar os testes:
python src/test_biblioteca.py


🤝 Contribuição

Contribuições são bem-vindas!
Para contribuir:

Faça um fork do repositório.

Crie um branch para sua feature (git checkout -b feature/nova-funcionalidade).

Faça commit das alterações.

Envie um pull request.


📜 Licença

Este projeto é distribuído sob a licença MIT.
Sinta-se livre para usá-lo e modificá-lo conforme necessário.


👤 Autor

Desenvolvido por [Edson de Oliveira Vieira]
📧 Contato: [edson.vieira@faculdadeimpacta.com.br]