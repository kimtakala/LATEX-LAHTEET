*** Settings ***
Resource  resource.robot
Suite Setup      Open And Configure Browser
Suite Teardown   Close Browser
Test Setup       Reset Sources

*** Test Cases ***
After adding a book, there is one
    Go To  ${HOME_URL}
    Click Add Source
    Select Type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Page Should Contain Key  tolkien
    Page Should Contain Title  Taru sormusten herrasta
    Page Should Contain Author  JRR Tolkien
    Page Should Contain Year  1948

After adding two books, there are two
    Go To  ${HOME_URL}
    Click Add Source
    Select Type  book
    Input Key  tolkien
    Input Title  Taru sormusten herrasta
    Input Author  JRR Tolkien
    Input Publisher  Otava
    Input Year  1948
    Publish Source

    Click Add Source
    Select Type  book
    Input Key  1984
    Input Title  Vuonna 1984
    Input Author  George Orwell
    Input Publisher  Tammi
    Input Year  1949
    Publish Source

    Page Should Contain Key  tolkien
    Page Should Contain Title  Taru sormusten herrasta
    Page Should Contain Author  JRR Tolkien
    Page Should Contain Year  1948
    Page Should Contain Key  1984  article-index=1
    Page Should Contain Title  Vuonna 1984  article-index=1
    Page Should Contain Author  George Orwell  article-index=1
    Page Should Contain Year  1949  article-index=1

*** Keywords ***
Input Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}