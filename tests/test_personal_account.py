from pages.personal_account import PersonalAccountPage


class TestPersonalAccount:
    def test_check_transition_by_clicking_on_personal_account_button(self, driver):
        personal_account = PersonalAccountPage(driver)

        personal_account.click_on_personal_account_button()
        personal_account.check_header_after_clicking_on_personal_account()

    def test_transition_from_personal_account_to_constructor_by_clicking_on_logo(self, driver):
        personal_account = PersonalAccountPage(driver)

        personal_account.click_on_personal_account_button()
        personal_account.click_on_logo()
        personal_account.check_header_after_transition_from_personal_account()

    def test_transition_from_personal_account_to_constructor_by_clicking_on_constructor(self, driver):
        personal_account = PersonalAccountPage(driver)

        personal_account.click_on_personal_account_button()
        personal_account.click_on_constructor()
        personal_account.check_header_after_transition_from_personal_account()