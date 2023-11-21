from pytest import fixture
from src.keyboard import Keyboard, MixinChangeLanguage

@fixture
def kb():
    return Keyboard('Light Project', 9600, 5)

def test_init(kb):
    assert kb.name == 'Light Project'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"

def test_change_lang(kb):
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"

def test_change_language_in_mixin():
    mix = MixinChangeLanguage()
    assert mix.change_lang("EN") == "RU"
    assert mix.change_lang("RU") == "EN"

# ============================= test session starts ==============================
# collecting ... collected 3 items
#
# test_keyboard.py::test_init PASSED                                       [ 33%]
# test_keyboard.py::test_change_lang PASSED                                [ 66%]
# test_keyboard.py::test_change_language_in_mixin PASSED                   [100%]
#
# ============================== 3 passed in 0.01s ===============================
#
# Process finished with exit code 0