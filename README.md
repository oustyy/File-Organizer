
# 📁 File Organizer

## 📖 Sobre o Projeto

**File Organizer** é um script Python projetado para organizar arquivos em uma pasta selecionada, classificando-os em subpastas com base em suas extensões. Ele também lida com arquivos duplicados, movendo-os para uma pasta específica, e remove pastas vazias ao final do processo. Com uma interface de linha de comando colorida e uma barra de progresso, o script torna a organização de arquivos eficiente e visualmente agradável. 📂

---

## ✨ Visão Geral

O **File Organizer** é ideal para usuários que desejam manter suas pastas organizadas automaticamente. Ele:
- Agrupa arquivos em pastas específicas com base em suas extensões (imagens, documentos, vídeos, etc.). 🗂️
- Move arquivos duplicados para uma pasta chamada `duplicados`, renomeando-os se necessário. 🔄
- Deleta arquivos `.nomedia` automaticamente. 🗑️
- Remove pastas vazias após a organização. 🧹
- Exibe um resumo detalhado do processo, incluindo tempo de execução, pastas criadas/deletadas e arquivos movidos/renomeados. 📊

---

## 🚀 Funcionalidades

- **Organização por Extensão**: Classifica arquivos em categorias predefinidas (imagens, vídeos, documentos, etc.). 📋
- **Tratamento de Duplicatas**: Move arquivos duplicados para a pasta `duplicados`, adicionando sufixos numéricos se necessário. 🔢
- **Remoção de Arquivos .nomedia**: Identifica e deleta automaticamente arquivos `.nomedia`. 🗑️
- **Criação de Pastas**: Cria automaticamente pastas para cada categoria de arquivo, se ainda não existirem. 📁
- **Remoção de Pastas Vazias**: Limpa pastas vazias após a organização. 🧹
- **Barra de Progresso**: Exibe o progresso da organização com a biblioteca `tqdm`. ⏳
- **Resumo do Processo**: Mostra estatísticas detalhadas ao final, incluindo tempo total, pastas criadas/deletadas e arquivos movidos/renomeados. 📈

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia         | Descrição                              |
|--------------------|----------------------------------------|
| **Python**         | Linguagem principal do script. 🐍      |
| **tkinter**        | Interface para seleção de pastas. 🖼️  |
| **colorama**       | Exibição de mensagens coloridas no terminal. 🌈 |
| **tqdm**           | Barra de progresso para acompanhamento. ⏳ |
| **os**             | Manipulação de arquivos e diretórios. 📂 |

---

## 📦 Como Executar o Projeto

### Pré-requisitos
- [Python 3.x](https://www.python.org/downloads/) instalado.
- Bibliotecas Python necessárias:
  - `tkinter` (geralmente incluído com o Python).
  - `colorama`
  - `tqdm`
- Um editor como [VS Code](https://code.visualstudio.com/) ou qualquer IDE Python.

### Passos para Configuração

1. **Clone o Repositório**  
   ```bash
   git clone https://github.com/seu-usuario/file-organizer.git
   cd file-organizer
   ```

2. **Instale as Dependências**  
   Dentro da pasta do projeto, execute:
   ```bash
   pip install colorama tqdm
   ```

3. **Execute o Script**  
   Execute o script principal:
   ```bash
   python main.py
   ```

4. **Selecione a Pasta**  
   Uma janela será aberta para selecionar a pasta que deseja organizar. Escolha a pasta e clique em "OK". O script começará a processar os arquivos automaticamente.

---

## 🌟 Estrutura do Projeto

```
FILE-ORGANIZER/
├── main.py                  # Script principal que executa a organização
├── README.md                # Documentação do projeto
├── .gitignore               # Arquivo para ignorar arquivos/pastas no Git
└── requirements.txt         # Lista de dependências do projeto
```

---

## 📋 Exemplo de Uso

Execute o script com `python main.py`.

Selecione uma pasta com arquivos variados (imagens, documentos, vídeos, etc.).

O script:
- Criará pastas como imagens, documentos, videos, etc., conforme necessário.
- Moverá os arquivos para suas respectivas pastas.
- Moverá duplicatas para a pasta `duplicados`, renomeando-as se necessário (ex.: `foto_1.jpg`).
- Deletará arquivos `.nomedia` e pastas vazias.
- Exibirá um resumo com o tempo total, pastas criadas/deletadas e arquivos movidos/renomeados.

### Exemplo de Saída no Terminal

```
======================================
Quantidade de arquivos: 150
======================================
Processando arquivos: |██████████████████████████| 150/150 [00:05<00:00]
Arquivo encontrado: foto.jpg
Formato: .jpg
Movendo para: imagens/foto.jpg
--------------------------------------------
Arquivo duplicado: documento.pdf
Formato: .pdf
Movendo para: duplicados/documento_1.pdf
--------------------------------------------
Removendo pasta vazia: pasta_antiga
======================================
Resumo do processo
Tempo total: 5.23 segundos
Pastas criadas: 8
Pastas deletadas: 3
Arquivos movidos: 145
Arquivos renomeados: 10
Arquivos deletados: 2
======================================
```

---

## 👥 Equipe de Desenvolvimento

Este projeto foi criado por:

| Nome     | Papel         | GitHub                    |
|----------|---------------|---------------------------|
| oustyy | Desenvolvedor | https://github.com/oustyy   |

---


