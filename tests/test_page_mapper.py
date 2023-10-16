from selenium.webdriver import Chrome
from page.pages import PageTodo

# Cria uma instância do ChromeDriver
browser = Chrome()
url = 'http://localhost:5000'


def create_task(title, description, driver):
    page = PageTodo(driver, url)
    page.open()
    page.todo.create_task(title, description)
    return page.tasks.task_list[0], page


def edit_task(title, description, driver):
    page = PageTodo(driver, url)
    page.todo.edit_task(title, description)
    return page.tasks.task_list[0]


def test_create_task():
    """
    Cenário: criar uma task
        Dado você esta na pagina todo
        Quando uma task é criada
        então a task deve estar na lista de Tasks
    """
    task, page = create_task('Teste', 'Testando', browser)
    assert task.title == 'Teste'
    assert task.description == 'Testando'


def test_edit_task():
    """
       Cenário: Editar uma task
           Dado você esta na pagina todo
           Quando uma task é criada
           E a task criada é editada
           então a task deve estar na lista de Tasks com os valores editados
       """

    task_edit = edit_task('Edit Test', 'Edit testando', browser)

    assert task_edit.title == 'Edit Test'
    assert task_edit.description == 'Edit testando'


def test_task_done():
    """
    Cenário: Concluir uma task
        Dado você esta na pagina todo
        Quando uma task criada
        E depois concluida
        então a task deve estar com o botão de concluir alterado
    """
    task, page = create_task('Teste', 'Testando', browser)

    task.do()
    text = page.tasks.task_list[0].done_text
    assert text == 'Concluído'


def test_task_delete():
    """
    Cenário: Deletar uma task
         Dado você esta na pagina Todo
         Quando uma task é criada
         E depois deletada
         Então a task não deve ser exibida na lista de tasks
    """

    task, page = create_task('Teste', 'Testando', browser)

    page.tasks.task_list[0].delete()
    tasks = page.tasks.task_list
    assert page.tasks.task_list[0] not in tasks

