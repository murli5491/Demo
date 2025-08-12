


Feature: orange CRM
  Scenario: login the application
    Given launch the browser
    When open the orange HRM
    And Enter UserName "Admin" And EnterPassword "admin123"
    And click on login button
    Then user must successfully login to the dashboard page

   Scenario Outline: : orange CRM with multiple parameter
    Given launch the browser
    When open the orange HRM
    And Enter UserName <username> And EnterPassword <password>
    And click on login button
    Then user must successfully login to the dashboard page

    Examples:
    | username | password |
    | Admin    | admin123 |
    | Admin    | admin342 |
    | Admin    | admin567 |