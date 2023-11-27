# for homework 6

# - если файл `items.csv`, из которого по умолчанию считываются данные,
# не найден → выбрасывается исключение `FileNotFoundError` с сообщением “_Отсутствует файл item.csv_"
# - если файл `item.csv` поврежден (например, отсутствует одна из колонок данных) → выбрасывается
# исключение `InstantiateCSVError` с сообщением “_Файл item.csv поврежден_”.
#
# Класс-исключение `InstantiateCSVError` реализуйте самостоятельно.

class InstantiateCSVError(Exception):
    """Общий класс исключения при ошибке инициации из csv-файла"""

    def __init__(self, *args):
        self.message = args[0] if args else\
            'Файл item.csv поврежден'

    def __str__(self):
        return self.message
