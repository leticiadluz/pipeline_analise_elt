import requests
from datetime import datetime
from airflow.hooks.base import BaseHook
from sqlalchemy import create_engine, text
import psycopg2

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
                        "address_number": user["address"]["number"],
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


def carregar_dados(dados):
    connection = BaseHook.get_connection("postgresss")
    connection_string = f"postgresql+psycopg2://{connection.login}:{connection.password}@{connection.host}:{connection.port}/{connection.schema}"
    engine = create_engine(connection_string)

    try:
        with engine.begin() as conn:  
            if "products" in dados and dados["products"]:
                for product in dados["products"]:
                    conn.execute(text("""
                        INSERT INTO PRODUCTS (PRODUCT_ID, TITLE, PRICE, PRODUCT_DESCRIPTION, CATEGORY, PRODUCT_IMAGE, RATING_RATE, RATING_COUNT)
                        VALUES (:product_id, :title, :price, :product_description, :category, :product_image, :rating_rate, :rating_count)
                        ON CONFLICT (PRODUCT_ID) DO NOTHING
                    """), product)

            if "carts" in dados and dados["carts"]:
                for cart in dados["carts"]:
                    conn.execute(text("""
                        INSERT INTO CARTS (CART_ID, USERS_ID, PURCHASE_DATE, PRODUCT_ID, PRODUCT_QUANTITY)
                        VALUES (:cart_id, :users_id, :purchase_date, :product_id, :product_quantity)
                    """), cart)

            if "users" in dados and dados["users"]:
                for user in dados["users"]:
                    conn.execute(text("""
                        INSERT INTO USERS (USERS_ID, EMAIL, FIRSTNAME, LASTNAME, PHONE, CITY, STREET, ADDRESS_NUMBER, LATITUDE, LONGITUDE)
                        VALUES (:users_id, :email, :firstname, :lastname, :phone, :city, :street, :address_number, :latitude, :longitude)
                        ON CONFLICT (USERS_ID) DO NOTHING
                    """), user)

        print("Dados carregados com sucesso!")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        raise
