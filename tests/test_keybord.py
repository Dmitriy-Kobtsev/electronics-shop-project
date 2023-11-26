from src import keyboard

def test_keyboard():
    kb = keyboard.Keyboard('Logiteck', 5000, 10)
    assert str(kb) == "Logiteck"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

    kb.language = 'RU'
    assert str(kb.language) == 'RU'
