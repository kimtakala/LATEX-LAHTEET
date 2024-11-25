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

Add a source, click delete and confirm
    Go To  ${HOME_URL}
    Click Add Source
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Wait Until Element Is Visible  messages
    Click Delete And Confirm
    Page Should Not Contain  Taru sormusten herrasta

Add two sources, delete and confirm both
    Go To  ${HOME_URL}
    Click Add Source
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Wait Until Element Is Visible  messages
    Click Add Source
    Input Key  1984
    Input Title  Vuonna 1984
    Input Author  George Orwell
    Input Publisher  Tammi
    Input Year  1949
    Publish Source

    Wait Until Element Is Visible  messages
    Click Delete On First And Confirm
    Page Should Not Contain  Taru sormusten herrasta
    Click Delete On Second And Confirm
    Page Should Not Contain  Poista

Add a source, click delete and then cancel
    Go To  ${HOME_URL}
    Click Add Source
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Wait Until Element Is Visible  messages
    Click Delete And Cancel
    Page Should Contain  Taru sormusten herrasta


*** Keywords ***
Click Add Source
    Click Button  add-source-btn

Click Delete And Confirm
    Click Button  delete-source-btn
    Handle Alert  action=ACCEPT

Click Delete On First And Confirm
    ${Title} =  Set Variable  Taru sormusten herrasta
    Click Button  xpath=//div[contains(text(), "Taru sormusten herrasta")]/following-sibling::form/child::button
    Handle Alert  action=ACCEPT

Click Delete On Second And Confirm
    ${Title} =  Set Variable  Vuonna 1984
    Click Button  xpath=//div[contains(text(), "Vuonna 1984")]/following-sibling::form/child::button
    Handle Alert  action=ACCEPT

Click Delete And Cancel
    Click Button  delete-source-btn
    Handle Alert  action=DISMISS

Publish Source
    Wait Until Element Is Visible  source-form-btn
    Click Button  source-form-btn

Input Key
    [Arguments]  ${key}
    Input Text  bibtex_key  ${key}

Input Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Input Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Input Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Input Year
    [Arguments]  ${year}
    Input Text  year  ${year}
