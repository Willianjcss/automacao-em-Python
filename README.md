# 🤖 Automação de Tarefas com Python – Cadastro Automático via Web

Este projeto em **Python** realiza uma automação completa: ele lê dados de um arquivo `.csv` e cadastra automaticamente essas informações em um site, simulando interações humanas (como preencher formulários e clicar em botões).

---

## 📂 Estrutura do Projeto

📁 automacao-tarefas/ 
├── dados.csv # Arquivo com os dados que serão processados 
├── bot.py # Script principal da automação 
└── README.md # Documentação do projeto


---

## ⚙️ Como Funciona

1. O script lê o arquivo `dados.csv` com as informações.
2. Para cada linha do CSV, ele executa a automação:
   - Abre o site automaticamente
   - Preenche os campos do formulário
   - Realiza o envio/cadastro
3. O processo é repetido para todos os registros do arquivo.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.13.1**
- `pandas` para leitura de dados
- `time` para da um tempo de uma ação para outra
- `pyautogui` para fazer pausas
---

## ▶️ Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt

🔐 Observações Importantes
Certifique-se de que o site de destino esteja acessível.

O código está preparado para evitar duplicidades e erros de preenchimento.

Para uso com autenticação, adicione suas credenciais no script (de forma segura).

📫 Contato
Se tiver dúvidas ou quiser contribuir com melhorias, entre em contato comigo aqui ou pelo LinkedIn. 😉
