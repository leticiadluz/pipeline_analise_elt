-- Codigo para criação das tabelas com os endpoint:
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
    CART_ID INT PRIMARY KEY,       
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
