from abc import abstractmethod
from src.item import Item


class MixinChangeLanguage:
    lang = "EN"

    def change_lang(self, current_language):
        if current_language == "EN":
            return "RU"
        else:
            return "EN"


class Keyboard(Item, MixinChangeLanguage):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = super().lang

    # напишем только геттер для language
    @property
    def language(self):
        return self.__language

    def change_lang(self, **kwargs):
        self.__language = super().change_lang(self.__language)
