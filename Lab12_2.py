class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data["birthdate"] < self.data["birthdate"]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data["birthdate"] > self.data["birthdate"]:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, phone_number):
        if self.data["phone_number"] == phone_number:
            return self.data
        if self.left is not None:
            left_result = self.left.find(phone_number)
            if left_result is not None:
                return left_result
        if self.right is not None:
            right_result = self.right.find(phone_number)
            if right_result is not None:
                return right_result
        return None

    def save(self):
        result = []
        if self.left:
            result.extend(self.left.save())
        result.append(self.data)
        if self.right:
            result.extend(self.right.save())
        return result

    @classmethod
    def load(cls, data):
        tree = cls()
        for node in data:
            tree.insert(node)
        return tree

def read_note():
    try:
        last_name = input("Прізвище: ")
        first_name = input("Ім'я: ")
        phone_number = input("Номер телефону: ")
        birthdate = list(map(int, input("Дата народження (дд,мм,рррр): ").split(',')))
        return {"last_name": last_name, "first_name": first_name, "phone_number": phone_number, "birthdate": birthdate}
    except ValueError:
        print("Помилка: Введіть правильний формат дати народження (дд,мм,рррр).")
        return None

def save_tree_to_file(tree, filename):
    try:
        with open(filename, "w") as file:
            for note in tree.save():
                file.write(f'{note["last_name"]},{note["first_name"]},{note["phone_number"]},{",".join(map(str, note["birthdate"]))}\n')
    except IOError:
        print("Помилка при збереженні файлу.")

def load_tree_from_file(filename):
    tree = Node()
    try:
        with open(filename, "r") as file:
            for line in file:
                last_name, first_name, phone_number, birthdate_str = line.strip().split(',', 3)
                birthdate = list(map(int, birthdate_str.split(',')))
                tree.insert({"last_name": last_name, "first_name": first_name, "phone_number": phone_number, "birthdate": birthdate})
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None
    except IOError:
        print("Помилка при читанні файлу.")
        return None
    return tree


def remove(self, phone_number, parent=None):
    if self.data["phone_number"] == phone_number:
        if self.left is not None and self.right is not None:
            self.data = self.right.find_min()
            self.right.remove(self.data["phone_number"], self)
        else:
            if parent is not None:
                if parent.left == self:
                    parent.left = self.left if self.left is not None else self.right
                else:
                    parent.right = self.left if self.left is not None else self.right
                self.left = None
                self.right = None
            else:
                if self.left is not None:
                    self.data = self.left.data
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.data = self.right.data
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    self.data = None
        return True
    elif self.left is not None and phone_number < self.data["phone_number"]:
        return self.left.remove(phone_number, self)
    elif self.right is not None and phone_number > self.data["phone_number"]:
        return self.right.remove(phone_number, self)
    return False


Node.remove = remove

def find_min(self):
    if self.left is not None:
        return self.left.find_min()
    return self.data

Node.find_min = find_min

def display_tree(self):
    if self.left:
        self.left.display_tree()
    display_note(self.data)
    if self.right:
        self.right.display_tree()

Node.display_tree = display_tree

def sort_tree_by_birthdate(self):
    notes = self.save()
    notes.sort(key=lambda x: x["birthdate"])
    return notes

Node.sort_tree_by_birthdate = sort_tree_by_birthdate

def display_note(note):
    print("Прізвище:", note["last_name"])
    print("Ім'я:", note["first_name"])
    print("Номер телефону:", note["phone_number"])
    print("Дата народження:", ",".join(map(str, note["birthdate"])))


def search_by_property(tree):
    print("Оберіть властивість для пошуку:")
    print("1. Прізвище та ім'я")
    print("2. Дата народження")
    print("3. Номер телефону")
    choice = input("Введіть номер варіанту: ")

    if choice == "1":
        last_name = input("Введіть прізвище: ")
        first_name = input("Введіть ім'я: ")
        result = tree.find_by_name(first_name, last_name)
    elif choice == "2":
        birthdate = list(map(int, input("Дата народження (дд,мм,рррр): ").split(',')))
        result = tree.find_by_birthdate(birthdate)
    elif choice == "3":
        phone_number = input("Введіть номер телефону: ")
        result = tree.find(phone_number)
    else:
        print("Невірний вибір, спробуйте ще раз.")
        return

    if result is not None:
        display_note(result)
    else:
        print("Такої людини немає")
def find_by_name(self, first_name, last_name):
        if self.data["first_name"] == first_name and self.data["last_name"] == last_name:
            return self.data
        if self.left is not None:
            left_result = self.left.find_by_name(first_name, last_name)
            if left_result is not None:
                return left_result
        if self.right is not None:
            right_result = self.right.find_by_name(first_name, last_name)
            if right_result is not None:
                return right_result
        return None
    
def find_by_birthdate(self, birthdate):
        if self.data["birthdate"] == birthdate:
            return self.data
        if self.left is not None:
            left_result = self.left.find_by_birthdate(birthdate)
            if left_result is not None:
                return left_result
        if self.right is not None:
            right_result = self.right.find_by_birthdate(birthdate)
            if right_result is not None:
                return right_result
        return None

Node.find_by_name = find_by_name
Node.find_by_birthdate = find_by_birthdate
def remove_by_property(tree):
    print("Оберіть властивість для видалення:")
    print("1. Прізвище та ім'я")
    print("2. Дата народження")
    print("3. Номер телефону")
    choice = input("Введіть номер варіанту: ")

    if choice == "1":
        last_name = input("Введіть прізвище: ")
        first_name = input("Введіть ім'я: ")
        removed = tree.remove_by_name(first_name, last_name)
    elif choice == "2":
        birthdate = list(map(int, input("Дата народження (дд,мм,рррр): ").split(',')))
        removed = tree.remove_by_birthdate(birthdate)
    elif choice == "3":
        phone_number = input("Введіть номер телефону: ")
        removed = tree.remove(phone_number)
    else:
        print("Невірний вибір, спробуйте ще раз.")
        return

    if removed:
        print("Запис видалено")
    else:
        print("Такої людини немає")

def remove_by_name(self, first_name, last_name, parent=None):
    if self.data["first_name"] == first_name and self.data["last_name"] == last_name:
        return self.remove(self.data["phone_number"], parent)
    if self.left is not None:
        left_result = self.left.remove_by_name(first_name, last_name, self)
        if left_result:
            return True
    if self.right is not None:
        right_result = self.right.remove_by_name(first_name, last_name, self)
        if right_result:
            return True
    return False

def remove_by_birthdate(self, birthdate, parent=None):
    if self.data["birthdate"] == birthdate:
        return self.remove(self.data["phone_number"], parent)
    if self.left is not None:
        left_result = self.left.remove_by_birthdate(birthdate, self)
        if left_result:
            return True
    if self.right is not None:
        right_result = self.right.remove_by_birthdate(birthdate, self)
        if right_result:
            return True
    return False

Node.remove_by_name = remove_by_name
Node.remove_by_birthdate = remove_by_birthdate

tree = Node()
while True:
        print("Меню:")
        print("1. Додати запис")
        print("2. Знайти запис")
        print("3. Зберегти дерево в файл")
        print("4. Завантажити дерево з файлу")
        print("5. Видалити запис")
        print("6. Перегляд записів")
        print("7. Сортування записів за датою народження: ")
        print("0. Вихід")

        choice = input("Введіть номер опції: ")
        
        if choice == "1":
            note = read_note()
            tree.insert(note)
        elif choice == "2":
            search_by_property(tree)
        elif choice == "3":
            filename = input("Введіть ім'я файлу: ")
            save_tree_to_file(tree, filename)
            print("Дерево збережено")
        elif choice == "5":
            remove_by_property(tree)
        elif choice == "6":
            print("Перегляд записів:")
            tree.display_tree()
        elif choice == "7":
            print("Сортування записів за датою народження:")
            sorted_notes = tree.sort_tree_by_birthdate()
            for note in sorted_notes:
                display_note(note)
        elif choice == "4":
            filename = input("Введіть ім'я файлу: ")
            loaded_tree = load_tree_from_file(filename)
            if loaded_tree is not None:
                tree = loaded_tree
                print("Дерево завантажено")
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")