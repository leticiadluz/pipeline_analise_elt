
"Estes comandos foram realizados diretamente no console web do Snowflake."
CREATE TABLE IF NOT EXISTS PRODUCTS (
    ID INT AUTOINCREMENT PRIMARY KEY,       
    TITLE VARCHAR(255),                    
    PRICE NUMBER(10, 2),                    
    DESCRIPTION VARCHAR,                   
    CATEGORY VARCHAR(100),                  
    IMAGE VARCHAR(2083),                    
    RATING_RATE NUMBER(3, 2),               
    RATING_COUNT INT                        
);

CREATE TABLE IF NOT EXISTS CARTS (
    ID INT AUTOINCREMENT PRIMARY KEY,       
    USER_ID INT,                            
    DATE TIMESTAMP,                         
    PRODUCT_ID INT,                         
    PRODUCT_QUANTITY INT                            
);


