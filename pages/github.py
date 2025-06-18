import allure
from selene import browser, by, have

class Github:

    @allure.step('Открыть главную страницу GitHub')
    def open(self):
        browser.open('/')
        return self

    @allure.step('Ввести в поиск имя репозитория {repo}')
    def search_repo(self, repo):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type(repo).press_enter()
        return self

    @allure.step('Перейти в репозиторий {repo}')
    def go_to_repo(self, repo):
        browser.element(by.link_text(repo)).click()
        return self

    @allure.step('Открыть вкладку Issues')
    def go_to_issue_tab(self):
        browser.element('#issues-tab').click()
        return self

    @allure.step('Проверить наличие Issue с названием {name}')
    def should_have_issue_name(self, name):
        browser.element('[data-testid=issue-pr-title-link]').should(have.exact_text(name))
        return self
