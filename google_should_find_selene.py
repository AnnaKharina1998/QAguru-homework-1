from selene import browser, have, by


def test_google_should_find_selene():
    browser.open('https://google.com')
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

    browser.quit()


def test_yandex_should_find_selene():
    browser.open('https://ya.ru/')
    browser.element(by.xpath("//input[@placeholder='Найдётся всё']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ul[@id='search-result']")).should(have.text('yashaka/selene'))

    browser.quit()


def test_duck_should_find_selene():
    browser.open('https://duckduckgo.com')
    browser.element(by.xpath("//input[@placeholder='Поиск без отслеживания']")).type('yashaka/selene').press_enter()
    browser.element(by.xpath("//ol[@class='react-results--main']")).should(have.text('yashaka/selene'))

    browser.quit()