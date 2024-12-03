*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Sources

*** Test Cases ***
At start there are no sources
    Go To  ${HOME_URL}
    Title Should Be  BibTex -lähdehallintatyökalu
    Page Should Contain  Ei lähteitä

Add a book source, click delete and confirm
    Go To  ${HOME_URL}
    Click Add Source
    Select From List By Value  id=add-field-type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Year  1948
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Publish Source

    Wait Until Element Is Visible  messages
    Click Delete And Confirm
    Sleep    0.1s
    Page Should Contain  Ei lähteitä

Add an article source, click delete and confirm
    Go To  ${HOME_URL}
    Click Add Source
    Select From List By Value  id=add-field-type  article
    Input Key  article1
    Input Title  Artikkeli
    Input Year  2010
    Input Author  Kirjoittajan Nimi
    Input Journal  Julkaisu
    Publish Source

    Wait Until Element Is Visible  messages
    Click Delete And Confirm
    Sleep    0.1s
    Page Should Contain  Ei lähteitä

Add a book source, click delete and then cancel
    Go To  ${HOME_URL}
    Click Add Source
    Select From List By Value  id=add-field-type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Year  1948
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Publish Source

    Wait Until Element Is Visible  messages
    Click Delete And Cancel
    Page Should Contain  Taru sormusten herrasta

Add book and article sources, delete and confirm both
    Go To  ${HOME_URL}
    Click Add Source
    Select From List By Value  id=add-field-type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Year  1948
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Publish Source

    Wait Until Element Is Visible  messages
    Click Add Source
    Select From List By Value  id=add-field-type  article
    Input Key  article1
    Input Title  Artikkeli 1
    Input Year  2010
    Input Author  Kirjoittajan Nimi
    Input Journal  Julkaisu
    Publish Source

    Wait Until Element Is Visible  messages
    Click Delete And Confirm
    Sleep    0.1s
    Click Delete And Confirm
    Sleep    0.1s
    Page Should Contain  Ei lähteitä


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

Input Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Input Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Input Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Input Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}
