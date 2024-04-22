from pages.base_page import BasePage
from data.data import Data


class AccountCreatePage(BasePage):
    page_url = Data.create_account_url
    title = 'Create New Customer Account'
