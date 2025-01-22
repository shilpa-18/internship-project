Feature: User can filter deals by specific Unit price range

  Scenario: User can filter the Secondary deals by Unit price range
    Given Open main page and Login
    Then Input "email" and "password" to Login to the page
    When Open “Secondary” option at the left side menu
    Then Verify right page opens
    And Open "Filters" and input the {lower_price} and {higher_price}
    Then Verify the price in all cards is inside the range