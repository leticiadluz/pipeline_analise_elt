"Estes comandos foram realizados diretamente no console web do Snowflake."
CREATE TABLE IF NOT EXISTS PRODUCTS (
    PRODUCT_ID INT AUTOINCREMENT PRIMARY KEY,       
    TITLE VARCHAR(255),                    
    PRICE NUMBER(10, 2),                    
    PRODUCT_DESCRIPTION VARCHAR,                   
    CATEGORY VARCHAR(100),                  
    PRODUCT_IMAGE VARCHAR(2083),                    
    RATING_RATE NUMBER(3, 2),               
    RATING_COUNT INT                        
);

CREATE TABLE IF NOT EXISTS CARTS (
    CART_ID INT AUTOINCREMENT PRIMARY KEY,       
    USERS_ID INT,                            
    PURCHASE_DATE TIMESTAMP,                         
    PRODUCT_ID INT,                         
    PRODUCT_QUANTITY INT                            
);

CREATE TABLE IF NOT EXISTS USERS (
    USERS_ID INT AUTOINCREMENT PRIMARY KEY,               
    EMAIL VARCHAR(255),    
    FIRSTNAME VARCHAR(100),         
    LASTNAME VARCHAR(100),          
    PHONE VARCHAR(50),              
    CITY VARCHAR(100),              
    STREET VARCHAR(255),            
    ADDRESS_NUMBER INT,                    
    LATITUDE FLOAT,                 
    LONGITUDE FLOAT                 
);




