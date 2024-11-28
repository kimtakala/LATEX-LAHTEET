*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Sources

*** Test Cases ***
After adding an article, there is one
    Go To  ${HOME_URL}
    Click Add Source
    Select Type  article
    Input Key  einstein
    Input Title  Zur Elektrodynamik bewegter Körper
    Input Year  1906
    Input Author  Albert Einstein
    Input Journal  Annalen der Physik
    Input Volume  322
    Input Number  10
    Input Pages  891--921
    Input Month  December
    Publish Source

    Page Should Contain Key  einstein
    Page Should Contain Title  Zur Elektrodynamik bewegter Körper
    Page Should Contain Author  Albert Einstein
    Page Should Contain Year  1906

*** Keywords ***
Input Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Input Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Input Number
    [Arguments]  ${number}
    Input Text  number  ${number}

Input Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Input Month
    [Arguments]  ${month}
    Input Text  month  ${month}
