# 🛒 Rastreador de Preços - Amazon Brasil

Este projeto é uma automação em Python que utiliza o Selenium para buscar produtos na Amazon Brasil e salvar os resultados (nome e preço) em um arquivo CSV.

## 🚀 Tecnologias utilizadas

- Python 3.10+
- Selenium
- pandas
- ChromeDriver

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/rastreamento-preco.git
cd rastreamento-preco
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🧪 Como usar
1. Execute o script:

```bash
python main.py
```

2. O resultado será salvo em `precos.csv`.

## 📝 Exemplo de saída

| Produto                                    | Preço (R$) |
|--------------------------------------------|-------------|
| Monitor LG UltraGear 24” Full HD 180Hz     | 948         |
| Samsung T350 - Monitor Gamer 24"           | 567         |

## 📁 Estrutura do Projeto

```
📦 rastreamento-preco
┣ 📜 main.py
┣ 📜 requirements.txt
┗ 📜 precos.csv
```
