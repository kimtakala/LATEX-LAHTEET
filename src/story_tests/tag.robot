*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Sources

*** Test Cases ***
At start there are no sources
    Go To  ${HOME_URL}
    Title Should Be  BibTex -lähdehallintatyökalu

Can add tag
    # Add two sources

    Go To  ${HOME_URL}
    Click Add Source
    Select Type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Year  1948
    Input Publisher  Otava
    Publish Source

    Click Add Source
    Select Type  book
    Input Key  tolkien2
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Year  1948
    Input Publisher  Otava
    Publish Source

    Page Should Contain  tolkien
    Page Should Contain  tolkien2


    Click Button  css:article:first-child button.add-tag
    Input Text  name  tagi1
    Publish Tag

    Click Button  css:article:first-child button.add-tag
    Input Text  name  tagi2
    Publish Tag

    Click Button  css:article:last-child button.add-tag
    Input Text  name  tagi3
    Publish Tag

    Page Should Contain  tagi1
    Page Should Contain  tagi2
    Page Should Contain  tagi3

Can delete tag
    Go To  ${HOME_URL}
    Click Add Source
    Select Type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Year  1948
    Input Publisher  Otava
    Publish Source

    Page Should Contain  tolkien

    Click Button  css:article:first-child button.add-tag
    Input Text  name  tagi1
    Publish Tag
    Click Button  css:article:first-child .tags .tag button.delete
    Page Should Not Contain  tagi1

*** Keywords ***
Input Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}
