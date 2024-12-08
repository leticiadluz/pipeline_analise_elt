import requests
from datetime import datetime

def dados_api():
    url_base = "https://fakestoreapi.com"
    endpoints = ["products", "carts", "users"]
    dados_extraidos = {}

    for endpoint in endpoints:
        url = f"{url_base}/{endpoint}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            
            if endpoint == "products":
                produtos_transformados = []
                for product in dados:
                    produtos_transformados.append({
                        "product_id": product["id"],
                        "title": product["title"],
                        "price": product["price"],
                        "product_description": product["description"], 
                        "category": product["category"],
                        "product_image": product["image"], 
                        "rating_rate": product["rating"]["rate"],
                        "rating_count": product["rating"]["count"]
                    })
                    dados = produtos_transformados

            elif endpoint == "carts":
                carrinhos_transformados = []
                for cart in dados:
                    cart_id = cart["id"]
                    users_id = cart["userId"]
                    date = cart["date"]
                    purchase_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")
                    for product in cart["products"]:
                        carrinhos_transformados.append({
                            "cart_id": cart_id,
                            "users_id": users_id,
                            "purchase_date": purchase_date,
                            "product_id": product["productId"],
                            "product_quantity": product["quantity"]
                        })
                dados = carrinhos_transformados
            
            elif endpoint == "users":
                usuarios_transformados = []
                for user in dados:
                    usuarios_transformados.append({
                        "users_id": user["id"],
                        "email": user["email"],
                        "firstname": user["name"]["firstname"],
                        "lastname": user["name"]["lastname"],
                        "phone": user["phone"],
                        "city": user["address"]["city"],
                        "street": user["address"]["street"],
                        "adress_number": user["address"]["number"],
                        "latitude": user["address"]["geolocation"]["lat"],
                        "longitude": user["address"]["geolocation"]["long"]
                    })
                dados = usuarios_transformados
            dados_extraidos[endpoint] = dados
            print(f"Dados do endpoint '{endpoint}' extraídos e transformados com sucesso.")
        else:
            print(f"Erro ao acessar '{endpoint}': {resposta.status_code}")
            dados_extraidos[endpoint] = None

    return dados_extraidos

'''
teste = dados_api()

for endpoint, content in teste.items():
    print(f"\nDados do endpoint {endpoint}:")
    if content:
        print(content) 
    else:
        print(f"Nenhum dadoretornado para o endpoint {endpoint}.")'''
