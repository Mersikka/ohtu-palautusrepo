
*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  mio
    Set Password  miomio123
    Set PW Confirmation  miomio123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mi
    Set Password  mimi1234
    Set PW Confirmation  mimi1234
    Click Button  Register
    Register Should Fail With Message  Username should contain at least 3 characters
    

Register With Valid Username And Too Short Password
    Set Username  mio
    Set Password  m1o
    Set PW Confirmation  m1o
    Click Button  Register
    Register Should Fail With Message  Password should be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  mio
    Set Password  aaaaaaaaaaaaaaaaaaaa
    Set PW Confirmation  aaaaaaaaaaaaaaaaaaaa
    Click Button  Register
    Register Should Fail With Message  Password should contain at least 1 non-letter

Register With Nonmatching Password And Password Confirmation
    Set Username  mio
    Set Password  miomio123
    Set PW Confirmation  miomio125
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
   Set Username  kalle
   Set Password  moimoimoi123
   Set PW Confirmation  moimoimoi123
   Click Button  Register
   Register Should Fail With Message  Username already in use

*** Keywords ***
Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PW Confirmation
    [Arguments]  ${pw_conf}
    Input Password  password_confirmation  ${pw_conf}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
