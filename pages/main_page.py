from pages.base_page import BasePage


class MainPage(BasePage):

    SECONDARY_TAB = (By.ID,"w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b")
    SECONDARY_PAGE = (By.ID, "w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d4-7f66df43")
    FILTER_BUTTON = (By.XPATH, "//div[wized='openFiltersWindow']")
    APPLY_FILTER_BUTTON = (By.XPATH, 'a//[wized="applyFilterButtonMLS"]')


    def open_main_page(self):
        self.open_url('https://soft.reelly.io')

    def left_side_menu(self):
        self.click(MainPage.SECONDARY_TAB)

    def correct_page(self):
        self.click(MainPage.SECONDARY_PAGE)

    def open_filter(self):
        self.click(MainPage.FILTER_BUTTON)
        self.click(MainPage.APPLY_FILTER_BUTTON)

    def verify_prices_in_range(self, lower_price, higher_price):
        lower_range = 120000
        higher_range = 200000
        for card in range(lower_range, higher_range):
            if lower_price <= card <= higher_price:
                then


