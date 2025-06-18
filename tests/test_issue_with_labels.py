import allure
from allure_commons.types import Severity

@allure.tag("smoke")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Zaberuskina')
@allure.feature('GitHub Issues')
@allure.story('Проверка названия Issue в репозитории')
@allure.link('https://github.com', name='GitHub')
def test_with_labels_only():
    pass
