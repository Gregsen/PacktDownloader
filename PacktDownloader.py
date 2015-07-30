
__author__ = 'gkneitschel'

try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
except:
    raise ImportError("selenium package not found. Try running\n\t sudo pip install selenium")

EMAIL = ''
PASSWORD = ''
driver = webdriver.Firefox()

def startBrowser():
    driver.get('https://www.packtpub.com/packt/offers/free-learning')
    driver.maximize_window()
    driver.implicitly_wait(10)


def login():
    loginElement = driver.find_element_by_xpath('//*[@id="account-bar-login-register"]/a[1]/div')
    loginElement.click()

    email = driver.find_element_by_xpath("//*[@id='account-bar-form-login']/div[1]//input[@id='email']")
    email.send_keys(EMAIL)

    password = driver.find_element_by_xpath("//*[@id='account-bar-form-login']/div[1]//input[@id='password']")
    password.send_keys(PASSWORD)
    password.submit()

def claimEbook():
    claimBtn = driver.find_element_by_xpath('//*[@id="deal-of-the-day"]/div/div/div[2]/div[4]/div[2]/a/div/input')
    claimBtn.click()



def main():
    startBrowser()
    login()
    claimEbook()

if __name__ == "__main__":
    main()
