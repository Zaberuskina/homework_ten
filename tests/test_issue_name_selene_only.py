from selene import browser, by, have

def test_issue_name_selene_only():
    browser.open('https://github.com')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('Zaberuskina/homework_ten').press_enter()
    browser.element(by.link_text('Zaberuskina/homework_ten')).click()
    browser.element('#issues-tab').click()
    browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text('Test'))
