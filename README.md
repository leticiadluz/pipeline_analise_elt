## Tutorial: Como Instalar o Apache Airflow com Docker

Contexto: 
- Airflow tem várias dependências (banco de dados, executores, webserver, scheduler). Configurá-las manualmente pode ser complexo. Com o Docker, essas dependências são gerenciadas em contêineres, facilitando a configuração.  
- O Docker cria um ambiente isolado, garantindo que o Airflow funcione sem interferências de outros softwares instalados no sistema.  
- Configurações baseadas em Docker (via Docker Compose, por exemplo) podem ser facilmente compartilhadas entre equipes, garantindo que todos utilizem o mesmo ambiente, independentemente do sistema operacional.  
- O Airflow depende de várias bibliotecas que não têm suporte completo ou não funcionam adequadamente no Windows. Ele foi originalmente projetado para ambientes baseados em Linux/Unix, onde a maioria das suas dependências opera de forma nativa.

### 1. Instalação do Docker:

1.1 Instale o Docker  
Certifique-se de que o Docker está instalado em seu sistema. Você pode baixá-lo e instalá-lo a partir do site oficial: [Docker](https://www.docker.com/).

1.2 Usuários de Windows: Configure o WSL
Se você está utilizando o Windows, será necessário instalar e configurar o Windows Subsystem for Linux (WSL). Atualize o WSL utilizando o seguinte comando no terminal:
```bash
wsl --update
```
1.3 Testando o Docker: Após a instalação, teste se o Docker está funcionando corretamente executando no PowerShell:
```bash 
docker --version
```

Se o comando rodar com sucesso, o Docker está pronto para uso.


### 2. Instalação do Airflow:

2.1 Acesse o Site Oficial do Airflow: Entre no site oficial do [Airflow.](https://airflow.apache.org/)

2.2 Localize a Seção de Instalação: Clique em **Install Airflow** no menu do site. Selecione a versão desejada (no projeto, foi utilizada a versão 2.10.2).

2.3 Encontre as Instruções para Docker: Use a barra de pesquisa na documentação e procure por **docker**. Clique no resultado **Running Airflow in Docker**.

2.4 Obtenha o Arquivo docker-compose.yaml: Na página, localize a seção Fetching docker-compose.yaml. Clique no link para o arquivo docker-compose.yaml e faça o download para a pasta do seu projeto. Ou copie o conteúdo do arquivo e cole em um novo arquivo chamado docker-compose.yml dentro da pasta do projeto.

2.6 Estrutura de Diretórios: 
Crie as seguintes pastas no seu diretório de trabalho para configurar corretamente o ambiente:
- /dags - Pasta onde você armazenará seus DAGs (pipelines de dados).  
- /logs - Pasta onde os logs de execução serão salvos.  
- /plugins - Local para seus plugins personalizados.  

É importante criar as pastas manualmente para garantir controle sobre as permissões e evitar problemas de sincronização entre o host e o container. A pasta config é opcional e pode ser usada caso você queira adicionar configurações personalizadas

**AVISO: Dependendo do seu sistema operacional, pode ser necessário configurar o Docker para usar pelo menos 4,00 GB de memória para que os contêineres do Airflow funcionem corretamente.**
- Para alterar o uso de memória alocada para o Docker, **usuários Windows.** Abra um editor de texto e digite as configurações desejadas:
```bash
    [wsl2]
    memory=4GB
```
- Salve o arquivo como .wslconfig no diretório do seu usuário: C:\usarios\user.
- No campo Nome do arquivo, insira 
.wslconfig.
- No campo Tipo, escolha Todos os Arquivos.
- Clique em Salvar
- Abra o Prompt de Comando ou o PowerShell e execute:
```bash
wsl --shutdown
```
- Abra o terminal do WSL e digite o comando:
```bash
free -h
```
- O resultado será algo como:
```bash
        total    used   free
Mem:    4.0G     1.2G   1.8G
Swap:   1.0G     0.3G   0.7G
```
- total: Memória total alocada ao WSL.
- used: Memória sendo usada.
- free: Memória disponível.

O Comando abaixo também pode confirmar a quantidade de memória alocada:
```bash
docker info
```

2.7 Inicialize o ambiente do Airflow: 
Com o Docker aberto, abra o terminal bash na pasta onde está o arquivo docker-compose.yml e execute o comando:

```bash 
docker compose up airflow-init
```
Aguarde enquanto o Airflow instala as dependências e configurações necessárias.

2.8 Confirmação de Inicialização: 
Quando o processo for concluído, você verá uma mensagem como esta: 

```bash airflow-init_1       | Upgrades done
airflow-init_1       | Admin user airflow created
airflow-init_1       | 2.10.2
start_airflow-init_1 exited with code 0
```
2.9 Inicie os Serviços do Airflow: Para iniciar o Airflow, digite: 

```bash 
docker compose up -d
```
O parâmetro -d executa os contêineres em segundo plano, sem travar o terminal.

2.10 Você pode confirmar o estado dos contêineres com o seguinte comando:
 ```bash 
docker ps
```
Caso algum contêiner esteja apresentando falha, você pode acessar o terminal dentro contêiner do Airflow:

Isso permite inspecionar o ambiente diretamente.

 ```bash 
docker exec -it <container_name> bash
```

2.11 Acesse o Airflow: Aguarde a inicialização dos contêineres.Acesse o Airflow no navegador em: http://localhost:8080. Isso redirecionará para a tela de login do Airflow.

![alt text](imagens/airflow.png)

O usuário e senha padrão do Airflow são ambos **airflow**


