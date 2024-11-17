*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kallo  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle2  kalle123
    Output Should Contain  Username must only consist of letters from a to z

Register With Valid Username And Too Short Password
    Input Credentials  kalle  kalle12
    Output Should Contain  Username must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  kallekalle
    Output Should Contain  Password cannot consist of only letters

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command

Input New Command And Create User
    Input New Command
    Create User  k2  kalle
