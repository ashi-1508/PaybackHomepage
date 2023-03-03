from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class HomePageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values

        self.AboutusLinkElement = "//a[normalize-space()='About us']"
        self.EarnPointsButtonElement = "//a[@href='/shop-online']//img[contains(@class,'lazyloaded')]"
        self.ContactUsLinkElement = "//a[normalize-space()='contact us']"
        self.IWishToButtonElement = "//*[@class='input-group-btn search-panel']"
        self.EarnPointsLinkElement = "//a[@href='#earn']"
        self.SearchforProductAndDealsTextBoxElement = "//input[@id='pb-search-input']"



    def click_AboutUs_link(self):
        AboutusLink = self.driver.find_element(By.XPATH, self.AboutusLinkElement)
        AboutusLink.click()

    def click_EarnPoints_button(self):
        EarnPointsButton = self.driver.find_element(By.XPATH, self.EarnPointsButtonElement)
        EarnPointsButton.click()

    def click_ContactUs_link(self):
        ContactUsLink = self.driver.find_element(By.XPATH, self.ContactUsLinkElement)
        ContactUsLink.click()




    def click_IWishTo_button(self):
        IWishToButton = self.driver.find_element(By.XPATH, self.IWishToButtonElement)

        action = ActionChains(self.driver)
        action.move_to_element(IWishToButton)
        action.perform()
        IWishToButton.click()


        EarnPointsLink = self.driver.find_element(By.XPATH, self.EarnPointsLinkElement)
        action.move_to_element(EarnPointsLink)
        action.perform()
        EarnPointsLink.click()


    def click_SearchforProductAndDeals_TextBox(self, search):
        SearchforProductAndDealsTextBox = self.driver.find_element(By.XPATH, self.SearchforProductAndDealsTextBoxElement)
        SearchforProductAndDealsTextBox.send_keys(search)
        SearchforProductAndDealsTextBox.send_keys(Keys.ENTER)





















