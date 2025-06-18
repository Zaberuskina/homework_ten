import allure
from selene import browser, by, have

def test_issue_name_with_allure_steps():
    with allure.step('Открыть GitHub'):
        browser.open('https://github.com')

    with allure.step('Искать репозиторий Zaberuskina/homework_ten'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('Zaberuskina/homework_ten').press_enter()
        browser.element(by.link_text('Zaberuskina/homework_ten')).click()

    with allure.step('Открыть вкладку Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверить наличие Issue с названием "Test"'):
        browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text('Test'))
