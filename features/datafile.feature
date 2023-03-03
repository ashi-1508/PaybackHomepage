Feature: Payback Homepage

  Background:
      Given Chrome is opened and Payback app is opened


  Scenario Outline: Verify working of search option with valid data

     When Select from the drop down
     When User enter the <valid> firstdata
     Then User is displayed to the various options available for firstdata
     And Close the chrome
     Examples:
       | valid  |
       | Shoes  |


