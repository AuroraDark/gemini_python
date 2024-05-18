import google.generativeai as genai

from dotenv import load_dotenv
import os


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def categoriza_produtos(nome_produto, lista_categorias_validas):
    response = model.generate_content(f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.

            # Lista de Categorias Válidas
            {lista_categorias_validas.split(",")}

            # Formato da Saída
            Produto: Nome do Produto
            Categoria: apresente a categoria do produto

            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Categoria: Eletrônicos Verdes

            # Nome do Produto
            {nome_produto}
        """)
    return response.text

categorias_validas = input("Digite as categorias válidas: ")

while(True):
    nome_produto = input("Digite o nome de um produto: ")
    print(categoriza_produtos(nome_produto, categorias_validas))