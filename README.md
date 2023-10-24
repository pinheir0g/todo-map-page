# Todo Map Page

Principais interações da página mapeadas para o código.

## Sobre


Esse projeto é uma implementação de automação de testes que utiliza o padrão 
Page Object Model (POM) e uma Domain Specific Language (DSL) para interagir 
com o [Todo List.](https://github.com/pinheir0g/todo_app) 

O POM ajuda a melhorar a qualidade e a
manutenção do código de automação de testes, enquanto a DSL atua como uma 
interface de interação entre o webdriver do navegador e o código de teste.


## Requisitos


Como o `Todo Map Page` foi feito para testar o [Todo List](https://github.com/pinheir0g/todo_app) 
que criei, é preciso ter o projeto instalado e rodando localmente para que os testes funcionem.

### Instalação das dependências do projeto
Pode fazer a instalação utilizando poetry ou pip

- Usando pip
```Bash
pip install -r requirements.txt
```

- Usando poetry
```Bash
poetry install
```

## Configuração do ChromeDriver


Este projeto utiliza o `chromedriver-autoinstaller` para simplificar a configuração do ChromeDriver. 
Se você estiver usando o Google Chrome como o seu navegador de teste, o `chromedriver-autoinstaller` fará o download 
e a instalação automática do ChromeDriver, se necessário.

Para configurar o ChromeDriver, siga estas etapas:

1. Instale o `chromedriver-autoinstaller`:

   ```shell
   pip install chromedriver-autoinstaller
   ```
   ou
   ```shell
   poetry add chromedriver-autoinstaller
   ```

2. No arquivo [test_page_mapper.py](/tests/test_page_mapper.py) adicionar as seguintes linhas antes de
criar a instância do `Chrome()`:
   ```python
   import chromedriver_autoinstaller
   
   # Configura o chromedriver-autoinstaller para fazer o download e instalação automática
   chromedriver_autoinstaller.install()

## Testando

Antes de rodar os testes, certifique de ter instalado o [Todo List](https://github.com/pinheir0g/todo_app)
e que ele esteja rodando na sua máquina local.

### Utilizando Pytest
Na raiz do projeto, rode:
   ```bash
   pytest -v tests/test_page_mapper.py
   ```


## To-Do List e RTM

Antes de iniciar esse projeto, criei uma RTM para testar o TodoList e garantir que todos os requisitos fossem testados.

### Requirements Traceability Matrix (RTM)

Requirements Traceability Matrix (RTM) é um documento que mapeia e rastreia os requisitos do usuário com casos de teste. Captura todos os requisitos propostos pelo cliente e a rastreabilidade dos requisitos em um único documento. 

O principal objetivo da Matriz de Rastreabilidade de Requisitos é validar que todos os requisitos sejam verificados por meio de casos de teste, de forma que nenhuma funcionalidade seja desmarcada durante o teste de software.

Acesse [Requirements Traceability Matrix (RTM)](docs/RTM.pdf) para visualizar o documento.