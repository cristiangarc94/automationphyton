import self as self
from iBott.browser_activities import ChromeBrowser

#instanciamos la clase ChromeBrowser
driver = "C:\\path\\to\\chrome\\browser"
chrome = ChromeBrowser(PathDriver=driver, undetectable = True)

chrome.ignoreImages()
chrome.headless()
chrome.saveCookies()
proxy = "192.222.90.12:8900"
chrome. setProxy(proxy)

user_agent= "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
chrome.setUserAgent(user_agent)

user_profile= "C:\\path\\to\\user\\profile"
chrome.setprofile(user_profile)

chrome.open()

url = "https://google.com"
chrome.get(url)

if self.browser.element_exists("tag_name", "iframe"):
    iframe = self.browser.find_element_by_tag_name("iframe")
    browser.switch_to.frame(iframe)
    acceptButton = browser.find_element_by_xpath("//*[contains(text(),'Acepto')]")
    acceptButton.click()
    browser.switch_to.default_content()

Xpathelement = "/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input"


#localizar el elemento
elemento_buscador = browser.find_element_by_xpath(Xpathelement)

#hacemos click sobre el elemento
elemento_buscador.click()


#escribirmos el texto sobre el elemento
buscar_texto= "gatitos"
element.send_keys(buscar_texto)
#presionamos enter sobre el elemento
browser.enter(elemento_buscador)