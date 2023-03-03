
Feature: Payback Homepage

  Background:
      Given Chrome is opened and Payback app is opened



  Scenario: Verify About us Link

      When User clicks on About us
      Then It should be take to website introduction page
      And Close the chrome

   Scenario: Verify Earn Points Button

      When User clicks on Earn Points Button
      Then It should be take to Shop Online by Payback Across Leading Websites Page
      And Close the chrome


   Scenario: Verify Contact Us link

      When User clicks on Contact Us
      Then It should take to Contact us page.
      And Close the chrome

   Scenario Outline: Verify working of search option with valid data

     When Select from the drop down
     When User enter the <valid> data
     Then User is displayed to the various options available
     And Close the chrome
     Examples:
       | valid  |
       | Shoes  |

   Scenario Outline: Verify working of search option with invalid data

     When Select from the drop down
     When User enter the <invalid> data
     Then User is displayed with error message
     And Close the chrome
     Examples:
        | invalid  |
        | ###      |











