*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}     localhost:5001
${DELAY}      0.0 seconds
${HOME_URL}   http://${SERVER}
${RESET_URL}  http://${SERVER}/reset_db
${BROWSER}    chrome
${HEADLESS}   false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless

        # Tarvitaan ettei Lisää-nappi jää näytön ulkopuolelle
        Call Method  ${options}  add_argument  --window-size\=1920,1080
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Reset Sources
    Go To  ${RESET_URL}

*** Keywords ***
Click Add Source
    Wait Until Element Is Visible  add-source-btn
    Click Button  add-source-btn

Publish Source
    Wait Until Element Is Visible  source-form-btn
    Click Button  source-form-btn

Publish Tag
    Wait Until Element Is Visible  tag-form-btn
    Click Button  tag-form-btn

Select Type
    [Arguments]  ${type}
    Select From List By Value  id=add-field-type  ${type}

Input Key
    [Arguments]  ${key}
    Input Text  bibtex_key  ${key}

Input Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Input Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Input Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Page Should Contain Key
    [Arguments]  ${key}  ${article-index}=0
    Wait Until Element Is Visible  key-${article-index}
    Element Should Contain  key-${article-index}  ${key}

Page Should Not Contain Key
    [Arguments]  ${key}  ${article-index}=0
    Wait Until Element Is Visible  key-${article-index}
    Element Should Not Contain  key-${article-index}  ${key}

Page Should Contain Title
    [Arguments]  ${title}  ${article-index}=0
    Wait Until Element Is Visible  title-${article-index}
    Element Should Contain  title-${article-index}  ${title}

Page Should Contain Author
    [Arguments]  ${author}  ${article-index}=0
    Wait Until Element Is Visible  author-${article-index}
    Element Should Contain  author-${article-index}  ${author}

Page Should Contain Year
    [Arguments]  ${year}  ${article-index}=0
    Wait Until Element Is Visible  year-${article-index}
    Element Should Contain  year-${article-index}  ${year}

Page Should Contain Message
    [Arguments]  ${message}
    Wait Until Element Is Visible  message
    Element Should Contain  message  ${message}
