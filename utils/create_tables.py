from airflow.hooks.base import BaseHook
from sqlalchemy import create_engine, text

def criar_tabelas():
    connection = BaseHook.get_connection("postgresss")
    connection_string = f"postgresql+psycopg2://{connection.login}:{connection.password}@{connection.host}:{connection.port}/{connection.schema}"
    engine = create_engine(connection_string)

    sql_create_tables = """
    CREATE TABLE IF NOT EXISTS PRODUCTS (
        PRODUCT_ID INT PRIMARY KEY,       
        TITLE VARCHAR(255),                    
        PRICE NUMERIC(10, 2),                    
        PRODUCT_DESCRIPTION TEXT,                   
        CATEGORY VARCHAR(100),                  
        PRODUCT_IMAGE TEXT,                    
        RATING_RATE NUMERIC(3, 2),               
        RATING_COUNT INT                        
    );

    CREATE TABLE IF NOT EXISTS CARTS (
        CART_ID INT,       
        USERS_ID INT,                            
        PURCHASE_DATE DATE,                         
        PRODUCT_ID INT,                         
        PRODUCT_QUANTITY INT
    );

    CREATE TABLE IF NOT EXISTS USERS (
        USERS_ID INT PRIMARY KEY,               
        EMAIL VARCHAR(255),    
        FIRSTNAME VARCHAR(100),         
        LASTNAME VARCHAR(100),          
        PHONE VARCHAR(50),              
        CITY VARCHAR(100),              
        STREET VARCHAR(255),            
        ADDRESS_NUMBER INT,                    
        LATITUDE DOUBLE PRECISION,                 
        LONGITUDE DOUBLE PRECISION                 
    );
    """
    try:
        with engine.begin() as conn:
            print("Acessando o banco.")
            conn.execute(text(sql_create_tables))
            print("Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")

