# Создаем проект по тестированию сайта https://magento.softwaretestingboard.com/
# Проект должен быть создан с использованием паттерна Page-Object Model (POM)
#
# Задание
# Создать по три теста для каждой из этих страниц:
#
# https://magento.softwaretestingboard.com/customer/account/create/
# https://magento.softwaretestingboard.com/collections/eco-friendly.html
# https://magento.softwaretestingboard.com/sale.html
# Тесты - на вашу фантазию. Они могут проверять что угодно: наличие элементов, текст элементов, валидацию введённых данных, ....
#
# Проект создавайте так же как я создавал на занятии - в корне нашего проекта создайте папку test_UI_unique_name
import time

from playwright.sync_api import Page, expect, sync_playwright
import allure
import re


class Data:
    #URLs
    base_url = 'https://magento.softwaretestingboard.com/'
    create_account_url = 'customer/account/create/'
    eco_friendly_url = 'collections/eco-friendly.html'
    sale_url = 'sale.html'

    #LOCATORS
    #BASE PAGE LOCATORS
    linkWhatsNew = "page.locator('#ui-id-3')"
    linkSales = "page.locator('#ui-id-8')"
    linkCreateAccount = "page.get_by_role('link','Account')"
    header_h1 = "h1"

    #CREATE ACCOUNT PAGE LOCATORS
    # field_first_name = "self.page.locator('#firstname')"
    field_first_name = "#firstname"
    field_last_name = "#lastname"
    field_email = "#email_address"
    field_password = "#password"
    field_password_confirm = "#password-confirmation"
    button_submit = "button[title=\'Create an Account\']"


    #ECO FRIENDLY PAGE LOCATORS
    goods_titles = "a.product-item-link"
    page_limiter = "#limiter"
    next_page = "a.action.next"
    page1_item1 = "Ana Running Short"
    page1_item2 = "Tiffany Fitness Tee"
    page1_item3 = "Atlas Fitness Tank"
    page2_item1 = "Chaz Kangeroo Hoodie"


    #SALES PAGE LOCATORS
    dealsWomen = 'span.more.button'
    dealsMen = "//strong[contains(@class, 'title') and contains(text(), 'Men\’s Bargains')]"
    dealsLuma = "//strong[contains(@class, 'title') and contains(text(), 'Luma Gear Steals')]"
    discont20Percent = "//strong[contains(@class, 'title') and contains(text(), '20% OFF')]"
    discont50Uds = "//strong[contains(@class, 'title') and contains(text(), 'Spend $50 or more')]"
    dealsTees = "//strong[contains(@class, 'title') and contains(text(), 'You can\'t have too many tees')]"


class BasePage:
    root_url = Data.base_url
    page_url = None
    title = 'Home Page'

    def __init__(self, page: Page):
        self.page = page

    def open(self, timeout=5000):
        if self.page_url:
            self.page.goto(f'{self.root_url}{self.page_url}')
        else:
            self.page.goto(self.root_url)
    def check_title(self, title: str, timeout=5000):
        expect(self.page).to_have_title(title)

    def check_url(self, url: str, timeout=5000):
        expect(self.page).to_have_url(url)

    def check_header_h1(self, header: str, timeout=5000):
        page_header = self.page.locator(Data.header_h1).text_content().strip()
        assert page_header == header

    def check_element(self, element_locator, timeout=5000):
        page_element = self.page.locator(element_locator)
        return page_element

    def check_elements(self, element_locator, product_text, timeout=5000):
        page_elements = self.page.locator(element_locator)
        element_texts = page_elements.all_text_contents()
        element_is_found = False
        for element in element_texts:
            item = element.strip()
            if item == product_text:
                # print(item)
                element_is_found = True
                assert item == product_text

        if element_is_found is False:
            raise Exception(f"No such element found: {product_text}")


    def change_page_items_number(self, preset_value, timeout=10000):
        # self.page.locator(element_locator)
        self.page.wait_for_selector(Data.page_limiter, state="attached")
        self.page.locator(Data.page_limiter).last.select_option(preset_value)
        # time.sleep(15)
        self.page.wait_for_load_state("networkidle")


class AccountCreatePage(BasePage):
    page_url = Data.create_account_url
    title = 'Create New Customer Account'


class EcoFriendlyPage(BasePage):
    page_url = Data.eco_friendly_url
    title = 'Eco Friendly'


class SalePage(BasePage):
    page_url = Data.sale_url
    title = 'Sale'


# tests

@allure.testcase(Data.base_url, 'Test start page')
def test_start_page(page: Page):
    page = BasePage(page)
    page.open()
    page.check_url(Data.base_url)
    page.check_title(page.title)
    page.check_header_h1('Home Page')


@allure.testcase(Data.create_account_url, 'Test create account page')
def test_create_account_page(page: Page):
    page = AccountCreatePage(page)
    page.open()
    page.check_url(f'{Data.base_url}{Data.create_account_url}')
    page.check_title(page.title)

    page.check_element(Data.field_first_name).is_editable()
    page.check_element(Data.field_last_name).is_editable()
    page.check_element(Data.field_email).is_editable()
    page.check_element(Data.field_password).is_editable()
    page.check_element(Data.field_password_confirm).is_editable()
    page.check_element(Data.button_submit).is_enabled()


@allure.testcase(Data.eco_friendly_url, 'Test eco-friendly page')
def test_eco_friendly_page(page: Page):
    page = EcoFriendlyPage(page)
    page.open()
    page.check_url(f'{Data.base_url}{Data.eco_friendly_url}')
    page.check_title(page.title)
    # page.change_page_items_number('36')
    # page.check_element(Data.page_limiter).last.select_option("36")

    page.check_elements(Data.goods_titles, Data.page1_item1)
    page.check_elements(Data.goods_titles, Data.page1_item2)
    page.check_elements(Data.goods_titles, Data.page1_item3)
    page.check_element(Data.next_page).last.click()
    page.check_elements(Data.goods_titles, Data.page2_item1)
    page.check_elements(Data.goods_titles, 'Bruno Compete Hoodie')


@allure.testcase(Data.sale_url, 'Test sales page')
def test_sales_page(page: Page):
    page = SalePage(page)
    page.open()
    page.check_url(f"{Data.base_url}{Data.sale_url}")
    page.check_title(page.title)

    page.check_element(Data.dealsWomen).is_visible()
    page.check_element(Data.dealsMen).is_visible()
    page.check_element(Data.dealsLuma).is_visible()
    page.check_element(Data.discont20Percent).is_visible()
    page.check_element(Data.discont50Uds).is_visible()

#pytest --alluredir=allure-results
#allure serve