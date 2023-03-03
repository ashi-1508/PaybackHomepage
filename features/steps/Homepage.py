from behave import *
from hamcrest import *
import time


from features.pages.homepageclass import HomePageClass
from Dtadrivenfile.ExcelUtils import ExcelUtils
from features.utility.ConfigClass import ConfigClass

@given(u'Chrome is opened and Payback app is opened')

def step_impl(context):
    expectedTitle = "Largest Multi-brand Loyalty Program in India - PAYBACK"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))

@when(u'User clicks on About us')
def step_impl(context):
    homepage = HomePageClass(context.driver)
    homepage.click_AboutUs_link()

@then(u'It should be take to website introduction page')
def step_impl(context):
    expectedTitle = 'About PAYBACK - Largest Rewards Program in India'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(1)

@then(u'Close the chrome')
def step_impl(context):
    context.driver.quit()




@when(u'User clicks on Earn Points Button')
def step_impl(context):
    homepage = HomePageClass(context.driver)
    homepage.click_EarnPoints_button()

@then(u'It should be take to Shop Online by Payback Across Leading Websites Page')
def step_impl(context):
    expectedTitle = "Online Shopping: Best Deals, Offers, Earn Points - PAYBACK"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(1)




@when(u'User clicks on Contact Us')
def step_impl(context):
    homepage = HomePageClass(context.driver)
    homepage.click_ContactUs_link()

@then(u'It should take to Contact us page.')
def step_impl(context):
    expectedTitle = 'Contact Us - PAYBACK'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(1)




@when(u'Select from the drop down')
def step_impl(context):
    homepage = HomePageClass(context.driver)
    homepage.click_IWishTo_button()
    time.sleep(5)


@when("User enter the {variable} data")
def step_impl(context, variable):
    homepage = HomePageClass(context.driver)
    homepage.click_SearchforProductAndDeals_TextBox(variable)
    time.sleep(5)

@then(u'User is displayed to the various options available')
def step_impl(context):
    expectedTitle = 'Search Product List'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))




@then(u'User is displayed with error message')
def step_impl(context):
    expectedTitle = 'noresult'
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))




@when("User enter the {data} firstdata")
def step_impl(context, data):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")

    data = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 1)

    homepage = HomePageClass(context.driver)
    homepage.click_SearchforProductAndDeals_TextBox(data)
    time.sleep(5)

@then("User is displayed to the various options available for firstdata")
def step_impl(context):

    expectedTitle = 'Search Product List'
    actualTitle = context.driver.title
    print(actualTitle)

    try:
        if (expectedTitle == actualTitle):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 2, "Passed")
        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 2, "Failed")
            assert False
        time.sleep(2)
    finally:
        pass









