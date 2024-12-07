import requests

def fetch_data_from_api():
    base_url = "https://fakestoreapi.com"
    endpoints = ["products", "carts"]
    extracted_data = {}

    for endpoint in endpoints:
        url = f"{base_url}/{endpoint}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            if endpoint == "products":
                for product in data:
                    # Processar 'rating'
                    rating = product.pop("rating", {})
                    product["rating_rate"] = rating.get("rate")
                    product["rating_count"] = rating.get("count")
            
            elif endpoint == "carts":
                transformed_carts = []
                for cart in data:
                    cart_id = cart["id"]
                    user_id = cart["userId"]
                    date = cart["date"]
                    for product in cart["products"]:
                        transformed_carts.append({
                            "cart_id": cart_id,
                            "user_id": user_id,
                            "date": date,
                            "product_id": product["productId"],
                            "quantity": product["quantity"]
                        })
                data = transformed_carts
            
            extracted_data[endpoint] = data
            print(f"Dados do endpoint '{endpoint}' extraídos com sucesso.")
        else:
            print(f"Erro ao acessar '{endpoint}': {response.status_code}")
            extracted_data[endpoint] = None

    return extracted_data

# Testando o código diretamente
'''data = fetch_data_from_api()  

for endpoint, content in data.items():
    print(f"\n--- Dados do endpoint '{endpoint}' ---")
    if content:
        print(content)  
    else:
        print(f"Nenhum dado foi retornado para o endpoint '{endpoint}'.")'''
