import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

import time


# Обработка параметров запуска командной строки
def pytest_addoption(parser):
    # Параметр браузер исполнитель
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    
    # Параметр язык страницы
    parser.addoption('--page_language', action='store', default="en",
                     help="Choose language. Example: es, en, ru...")

# Фикстура инициализация браузера, запускающаяся для каждого метода
@pytest.fixture(scope="function", autouse=True)
def browser(request):
    # Получаем параметры браузера и языка из командной строки
    browser_name = request.config.getoption("browser_name")
    page_language = request.config.getoption("page_language")
    browser = None

    # Выбор браузера в зависимости от параметра
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # Настройка опций запуска браузера
        options = webdriver.ChromeOptions()
        # Устанавливает предпочтительный язык для веб-страницы
        options.add_experimental_option('prefs', {'intl.accept_languages': page_language})
        # Запуск браузера в фоновом режиме
        options.add_argument('--headless')
        options.page_load_strategy = 'eager'
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = webdriver.FirefoxOptions()
        # Открыть браузер в безголовом режиме (без графического интерфейса)
        options.add_argument('--headless')
        options.page_load_strategy = 'eager'
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference('intl.accert_language', page_language)
        options.profile = firefox_profile
        browser = webdriver.Firefox(options=options)

    else:
    # Обработка искличения при неправельном указании параметра browser_name
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    #time.sleep(5)
    browser.quit()