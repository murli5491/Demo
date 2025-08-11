Feature: orange CRM
  Scenario: login the application
    Given launch the browser
    When open the orange HRM
    And Enter UserName "Admin" And EnterPassword "admin123"
    And click on login button
    Then user must successfully login to the dashboard page


