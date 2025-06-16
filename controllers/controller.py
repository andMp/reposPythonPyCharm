# 1️ Добавлять новую книгу в библиотеку.
# 2️ Просматривать все книги.
# 3️ Фильтровать книги по жанру.
# 4️ Выдавать книгу пользователю.
# 5️ Возвращать книгу в библиотеку.
# 6️ Просматривать список пользователей и выданные им книги.
# 7️ Сохранять данные в файл и загружать их при старте. (например, JSON или простая сериализация)

class Biblioteka_controller():
    def __init__(self,model_kn,model_kor, view):
        self.model_kn = model_kn
        self.model_kor = model_kor
        self.view = view
        self.sp_kn = []
        self.sp_kor = []

    def run(self):
        self.spi_kn = model_kn.zavant_z_file(self.model_kor)
        while True:
            self.view.start_menu()
            var = input('Оберіть бажану дію:')
            match var:
                case '1':
