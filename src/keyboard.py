from src.item import Item


class MixinLog:

    def __init__(self, language='EN'):
        self.language = language

    def change_lang(self):
        if self.language == "EN":
            self.language = 'RU'
        elif self.language == "RU":
            self.language = 'EN'


class Keyboard(Item, MixinLog):

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        lang_list = ['EN', 'RU']
        if value not in lang_list:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self._language = value



