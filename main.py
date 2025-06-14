from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configurar produto
produto = "monitor gamer"
url = f"https://www.amazon.com.br/s?k={produto.replace(' ', '+')}"

# Inicializar navegador
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)


# Acessar página
driver.get(url)
time.sleep(3)

dados = []

resultados = driver.find_elements(By.CSS_SELECTOR, "div.s-result-item")

for item in resultados:
    try:
        titulo = item.find_element(By.CSS_SELECTOR, "h2 span").text.replace(",", " ").strip()
        preco = item.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        dados.append({
            "Produto": titulo,
            "Preço (R$)": preco.replace(".", "").strip()
        })
    except:
        continue

# Fechar navegador
driver.quit()

# Mostrar os primeiros resultados no terminal
for d in dados[:5]:
    print(f"{d['Produto']} → R$ {d['Preço (R$)']}")

# Salvar em CSV
df = pd.DataFrame(dados)
df.to_csv("precos.csv", index=False, encoding='utf-8-sig', sep=';')
print(f"\nArquivo 'precos.csv' gerado com {len(df)} registros.")