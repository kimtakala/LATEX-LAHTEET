*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Sources

*** Test Cases ***
After adding an article, there is one
    Go To  ${HOME_URL}
    Click Add Source
    Select Type  inproceedings
    Input Key  salam
    Input Title  Weak and Electromagnetic Interactions
    Input Year  1968
    Input Author  Abdus Salam
    Input Book Title  Elementary particle theory
    Input Editor  Nils Svartholm
    Input Series  Cool Physics
    Input Pages  367-377
    Input Address  Aspenäsgarden, Lerum, Stockholm
    Input Month  May
    Input Organization  Nobel sr.
    Input Publisher  Almquist & Wiksell
    Input Volume  1
    Publish Source

    Page Should Contain Key  salam
    Page Should Contain Title  Weak and Electromagnetic Interactions
    Page Should Contain Author  Abdus Salam
    Page Should Contain Year  1968

*** Keywords ***
Input Book Title
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Input Editor
    [Arguments]  ${editor}
    Input Text  editor  ${editor}

Input Series
    [Arguments]  ${series}
    Input Text  series  ${series}

Input Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Input Address
    [Arguments]  ${address}
    Input Text  address  ${address}

Input Month
    [Arguments]  ${month}
    Input Text  month  ${month}

Input Organization
    [Arguments]  ${organization}
    Input Text  organization  ${organization}

Input Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Input Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}
