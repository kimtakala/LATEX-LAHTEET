*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Sources

*** Test Cases ***
At start there are no sources
    Go To  ${HOME_URL}
    Title Should Be  BibTex -lähdehallintatyökalu
    Page Should Not Contain  Poista

Source remains after refresh
    Go To  ${HOME_URL}
    Click Add Source
    Select Type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Year  1948
    Input Publisher  Otava
    Publish Source

    Reload Page

    Page Should Contain Key  tolkien
    Page Should Contain Title  Taru sormusten herrasta
    Page Should Contain Author  JRR Tolkien
    Page Should Contain Year  1948

Cannot add without key
    Go To  ${HOME_URL}
    Click Add Source
    Publish Source
    
    Page Should Contain Message  Avain vaaditaan

*** Keywords ***
Input Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}
