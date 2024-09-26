def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # здесь функция ничего не возвращает, но и ошибку не выдает


inner_function()  # здесь функция не работает
