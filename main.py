import time
import pandas as pd
from playwright.sync_api import sync_playwright

# Inicia o Playwright e o navegador
with sync_playwright() as p:
    # Use 'headless=False' para que o navegador abra
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Abrir o Google Maps
    page.goto("https://www.google.com/maps/")
    time.sleep(10)

    # Termo de busca
    busca = "locadoras de motos em São Paulo"
    
    # Encontra a barra de pesquisa usando o atributo 'id'
    barra_pesquisa = page.locator("#searchboxinput")
    barra_pesquisa.fill(busca)
    barra_pesquisa.press("Enter")
    time.sleep(5)

    # Lista para armazenar os resultados
    dados = []
    
    # Rola e captura dados
    scrollable_container = page.locator('div[role="main"]')

    for i in range(5):
        time.sleep(5)

        resultados = page.locator('.Nv2PK').all()
        for resultado in resultados:
            try:
                nome = resultado.locator('.qBF1Pd').inner_text()
            except:
                nome = ''

            try:
                endereco = resultado.locator('.rllt__details').inner_text().split("\n")[0]
            except:
                endereco = ''

            try:
                telefone = resultado.locator('.UsdlK').inner_text()
            except:
                telefone = ''

            dados.append({
                'Nome': nome,
                'Endereço': endereco,
                'Telefone': telefone
            })

        page.evaluate("document.querySelector('div[role=main]').scrollBy(0, 1000)")
        time.sleep(3)

    # O Playwright fecha o navegador automaticamente com o bloco 'with'
    
    # Exportar para Excel
    import os
print("Salvando a planilha na pasta:", os.getcwd())
df = pd.DataFrame(dados)
df.to_excel("empresas_google_maps.xlsx", index=False)

print("Planilha criada com sucesso!")
    