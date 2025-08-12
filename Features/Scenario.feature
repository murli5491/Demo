Feature: orange CRM
  Background: common step
    Given launch the browser
    When open the orange HRM
    And Enter UserName "Admin" And EnterPassword "admin123"
    And click on login button



Scenario: login to HRM application
    Then user must successfully login to the dashboard page

Scenario: click on admin button
    Then click on admin button






