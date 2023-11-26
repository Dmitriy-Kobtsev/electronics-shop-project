from src.item import Item


class MixinLog:

    def __init__(self, language='EN'):
        self._language = language

    def change_lang(self):
        if self._language == "EN":
            self._language = 'RU'
        elif self._language == "RU":
            self._language = 'EN'


class Keyboard(Item, MixinLog):

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        lang_list = ['EN', 'RU']
        if value not in lang_list:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        return self._language




