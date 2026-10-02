import allure


@allure.suite('....')
@allure.title('.....')
def test_recovery_by_phone(login_page):
    recovery_page = login_page.click_forgot()
    recovery_by_phone_page = recovery_page.click_recovery_by_phone()
    selected_country_code = recovery_by_phone_page.select_random_country()
    actual_country_code = recovery_by_phone_page.get_phone_field_value()
    assert selected_country_code == actual_country_code
