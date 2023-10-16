from page_objects.page_objects import Page
from .elements import Tasks, Todo


class PageTodo(Page):
    tasks = Tasks()
    todo = Todo()