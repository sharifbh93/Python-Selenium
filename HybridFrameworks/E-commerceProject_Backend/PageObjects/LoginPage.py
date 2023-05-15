from selenium.webdriver.common.by import By

class Login:
    textbox_useremail_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    linkText_logout = "Logout"

    def __init__(self, driver):
        self.driver = driver

    # Rest of the class code here


    def setUserEmail(self, useremail):
        self.driver.find_element(By.ID, self.textbox_useremail_id).clear()
        self.driver.find_element(By.ID,self.textbox_useremail_id).send_keys(useremail)

    def setUserPassword(self, userpassword):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(userpassword)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.linkText_logout).click()

