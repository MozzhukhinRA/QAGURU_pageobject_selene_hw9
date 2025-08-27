from QAGURU_pageobject_selene_hw9.for_high_level.validate_form import FormValidator
from QAGURU_pageobject_selene_hw9.for_high_level.open_html_path_high import RegistrationPage
from QAGURU_pageobject_selene_hw9.for_high_level.user import User


def test_requirement_form():

    get_send = RegistrationPage()
    user = User()
    form = FormValidator()

    # Заполнение регистрационной формы
    get_send.register_form(user)

    # Проверка заполнения формы
    form.validate_form(user)
