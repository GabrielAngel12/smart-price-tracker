import requests
from bs4 import BeautifulSoup
import re

# Los headers simulan que la petición viene de un navegador real para evitar bloqueos simples.
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,es;q=0.8'
}

def fetch_product_price(url: str) -> float | None:
    """
    Obtiene el HTML de la URL, extrae y limpia el precio del producto.
    
    Args:
        url: La URL de la página del producto.

    Returns:
        El precio como un float, o None si no se pudo encontrar.
    """
    try:
        response = requests.get(url, headers=HEADERS)
        # Lanza una excepción si la petición falló (ej. error 404, 500)
        response.raise_for_status() 
    except requests.RequestException as e:
        print(f"Error al hacer la petición a {url}: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # --- ESTA ES LA PARTE QUE DEBES ADAPTAR PARA CADA SITIO WEB ---
    # Intenta encontrar el precio. Buscamos por varias clases comunes.
    # Ejemplo para Amazon:
    price_whole_element = soup.find('span', {'class': 'a-price-whole'})
    price_fraction_element = soup.find('span', {'class': 'a-price-fraction'})

    if price_whole_element and price_fraction_element:
        price_str = f"{price_whole_element.get_text().strip()}{price_fraction_element.get_text().strip()}"
        # Limpiar el precio: quitar comas, símbolos de moneda y convertir a float
        # Usamos regex para encontrar solo los números y el punto decimal
        price_cleaned = re.sub(r'[^\d.]', '', price_str)
        try:
            return float(price_cleaned)
        except (ValueError, TypeError):
            return None
    
    print("No se pudo encontrar el precio con los selectores definidos.")
    return None

# Ejemplo de uso (puedes ejecutar este archivo directamente para probar)
if __name__ == '__main__':
    # Reemplaza esta URL con una URL de producto real de Amazon
    test_url = "https://www.amazon.com.mx/Cerave-Crema-Hidratante-16-454/dp/B07CHPWFXK/139-3758002-5124841?pd_rd_w=BA2hn&content-id=amzn1.sym.39b841eb-b9fa-4001-8647-a107484d25b9&pf_rd_p=39b841eb-b9fa-4001-8647-a107484d25b9&pf_rd_r=X8MT6F3XPK2PKMCJYKFC&pd_rd_wg=dMvJX&pd_rd_r=94dd2349-58c2-46b5-a9f6-be8cd8ffa4f2&pd_rd_i=B07CHPWFXK&th=1" 
    price = fetch_product_price(test_url)
    
    if price:
        print(f"El precio del producto es: ${price}")
    else:
        print("No se pudo obtener el precio.")