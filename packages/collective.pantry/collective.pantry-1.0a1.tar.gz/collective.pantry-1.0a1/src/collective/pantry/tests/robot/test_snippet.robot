# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s collective.pantry -t test_snippet.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src collective.pantry.testing.COLLECTIVE_PANTRY_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_snippet.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Test Setup
Test Teardown  Close all browsers


*** Variables ***

${BROWSER}              chrome
${HEADLESS}             ${true}

*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Snippet
  Given a logged-in site administrator
    and an add snippet form
   When I type 'My Snippet' into the title field
    and I submit the form
   Then a snippet with the title 'My Snippet' has been created

Scenario: As a site administrator I can view a Snippet
  Given a logged-in site administrator
    and a snippet 'My Snippet'
   When I go to the snippet view
   Then I can see the snippet title 'My Snippet'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add snippet form
  Go To  ${PLONE_URL}/++add++Snippet

a snippet 'My Snippet'
  Create content  type=Snippet  id=my-snippet  title=My Snippet


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the snippet view
  Go To  ${PLONE_URL}/my-snippet
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a snippet with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the snippet title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}

Test Setup
  ${options}=  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys, selenium.webdriver
  Run keyword if  '${HEADLESS}' == '${true}'  Call Method  ${options}  add_argument  headless
  Call Method  ${options}  add_argument  disable-extensions
  Call Method  ${options}  add_argument  start-maximized
  Create WebDriver  Chrome  chrome_options=${options}
