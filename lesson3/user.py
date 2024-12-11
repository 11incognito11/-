class User:
    # Конструктор принимает имя и фамилию
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Метод для вывода имени
    def print_first_name(self):
        print(self.first_name)

    # Метод для вывода фамилии
    def print_last_name(self):
        print(self.last_name)

    # Метод для вывода полного имени
    def print_full_name(self):
        print(self.first_name + ' ' + self.last_name)
