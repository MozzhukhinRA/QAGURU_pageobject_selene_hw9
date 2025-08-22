from QAGURU_pageobject_selene_hw9.for_high_level.validate_form import FormValidator
from QAGURU_pageobject_selene_hw9.for_high_level.open_html_path_high import PhotoPage, BrowserPage, RegistrationPage
from QAGURU_pageobject_selene_hw9.for_high_level.user import User


def test_requirement_form():
    photo_for_import = PhotoPage()
    personal_data = BrowserPage()
    get_send = RegistrationPage()
    user = User()
    form = FormValidator

    # заполнение личных данных
    personal_data.students_registration_first_name(user.first_name)
    personal_data.students_registration_last_name(user.last_name)

    # заполнение эл почты
    personal_data.students_registration_mail(user.mail)

    # выбор чекбокса Female
    personal_data.students_registration_gender(user.gender)

    # ввод номера телефона
    personal_data.students_registration_phone(user.phone)

    # ввод даты
    personal_data.students_registration_date_of_birth(user.year,user.moth,user.day)

    # заполнение области subject
    personal_data.students_registration_subject(user.sub)

    # выбор чекбокса Hobbies
    personal_data.students_registration_checkbox(user.hobbies)

    # загрузка файла
    personal_data.students_registration_photo(photo_for_import.import_file(user.picture))

    # заполнение Current Address
    personal_data.students_registration_address(user.address)

    # выбор штата
    personal_data.students_registration_state()

    # выбор города
    personal_data.students_registration_city()

    # вызов submit
    get_send.press_submit()

    # проверка формы
    form.validate_form(user)
