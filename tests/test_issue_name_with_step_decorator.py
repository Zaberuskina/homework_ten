from pages.github import Github

def test_issue_name_with_step_decorator():
    github = Github()
    github.open() \
          .search_repo('Zaberuskina/homework_ten') \
          .go_to_repo('Zaberuskina/homework_ten') \
          .go_to_issue_tab() \
          .should_have_issue_name('Test')
