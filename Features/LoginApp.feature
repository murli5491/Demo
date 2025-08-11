Feature: orange CRM
  Scenario: login the application

    Given launch the browser
    When open the orange HRM
    And Enter UserName "Admin" And EnterPassword "admin123"
    #And Click on login button
    Then verify login button is displayed
    #And close browser
