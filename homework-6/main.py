from src.item import Item

# Для такой работы программы необходимо удаление файла или его
# редактирование. Это проделано в тестовых целях, но в конечной версии,
# в коммите оставляю нормальный csv-файл

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # Traceback (most recent call last):
    #   File "/Users/andrejskovorodnikov/Desktop/electronics-shop-project/
    #   homework-6/main.py", line 9, in <module>
    #     Item.instantiate_from_csv()
    #   File "/Users/andrejskovorodnikov/Desktop/electronics-shop-project/
    #   src/item.py", line 97, in instantiate_from_csv
    #     raise FileNotFoundError('Отсутствует файл item.csv')
    # FileNotFoundError: Отсутствует файл item.csv
    #
    # Process finished with exit code 1

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден

    # Traceback (most recent call last):
    # File "/Users/andrejskovorodnikov/Desktop/electronics-shop-project/
    # homework-6/main.py", line 9, in <module>
    #   Item.instantiate_from_csv()
    # File "/Users/andrejskovorodnikov/Desktop/electronics-shop-project/
    # src/item.py", line 108, in instantiate_from_csv
    #   raise InstantiateCSVError
    # src.instantiate_csv_error.InstantiateCSVError: Файл item.csv поврежден
