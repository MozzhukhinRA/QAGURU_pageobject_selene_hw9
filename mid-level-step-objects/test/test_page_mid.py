from QAGURU_pageobject_selene_hw9.for_mid_level.open_html_path_mid import PhotoPage, BrowserPage, RegistrationPage


def test_requirement_form():
    photo_for_import = PhotoPage()
    personal_data = BrowserPage()
    get_send = RegistrationPage()

    # заполнение личных данных
    personal_data.students_registration_first_name('Ivan')
    personal_data.students_registration_last_name('Ivanov')

    # заполнение эл почты
    personal_data.students_registration_mail('Ivanov@mail.ru')

    # выбор чекбокса Female
    personal_data.students_registration_gender()

    # ввод номера телефона
    personal_data.students_registration_phone('9871234567')

    # ввод даты
    personal_data.students_registration_date_of_birth('2000', 'April')

    # заполнение области subject
    personal_data.students_registration_subject()

    # выбор чекбокса Hobbies
    personal_data.students_registration_checkbox()

    # загрузка файла
    personal_data.students_registration_photo(photo_for_import.import_file('photo.jpeg'))

    # заполнение Current Address
    personal_data.students_registration_address('publish')

    # выбор штата
    personal_data.students_registration_state()

    # выбор города
    personal_data.students_registration_city()

    # вызов submit
    get_send.press_submit()

    # проверка формы
    get_send.assert_form(
        'Ivan Ivanov',
        'Ivanov@mail.ru',
        'Other',
        '9871234567',
        '15 April,2000',
        'Arts, Accounting',
        'Sports',
        'photo.jpeg',
        'publish',
        'Uttar Pradesh Merrut'
    )
