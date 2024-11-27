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

After adding a source, there is one
    Go To  ${HOME_URL}
    Click Add Source
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Wait Until Element Is Visible  messages  
    Page Should Contain  Taru sormusten herrasta
    Page Should Contain  JRR Tolkien
    Page Should Contain  1948

After adding two sources, there are two
    Go To  ${HOME_URL}
    Click Add Source
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Click Add Source
    Input Key  1984
    Input Title  Vuonna 1984
    Input Author  George Orwell
    Input Publisher  Tammi
    Input Year  1949
    Publish Source

    Wait Until Element Is Visible  messages  
    Page Should Contain  Taru sormusten herrasta
    Page Should Contain  JRR Tolkien
    Page Should Contain  1948
    Page Should Contain  Vuonna 1984
    Page Should Contain  George Orwell
    Page Should Contain  1949

Source remains after refresh
    Go To  ${HOME_URL}
    Click Add Source
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Reload Page

    Wait Until Element Is Visible  messages  
    Page Should Contain  Taru sormusten herrasta
    Page Should Contain  JRR Tolkien
    Page Should Contain  1948

Cannot add without key
    Go To  ${HOME_URL}
    Click Add Source
    Publish Source
    
    Wait Until Element Is Visible  messages  
    Page Should Contain  Avain vaaditaan

*** Keywords ***
Click Add Source
    Click Button  add-source-btn

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
