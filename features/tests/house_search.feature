Feature: User can filter deals by specific Unit price range

  Scenario: User can filter the Secondary deals by Unit price range
    Given Open main page and Login
    Then Input shilpagt1808@gmail.com and password to Login to the page
    When Open “Secondary” option at the left side menu
    Then Verify right page opens
    Then Click on "Filters" at the top of the page
    Then Filter the products by price range from 1200000 to 2000000 AED
    Then Verify the price in all cards is inside the range
