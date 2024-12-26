import time  
from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager

class Instabot:
    def __init__(self, username, password):
        self.username = username  
        self.password = password  
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

    def comment(self, post_url, comment_text, num_comments):
        self.driver.get(post_url)
        time.sleep(3)
        for _ in range(num_comments):
            comment_area = self.driver.find_element(By.XPATH, '//textarea[@aria-label="Add a comment…"]')
            comment_area.send_keys(comment_text)
            self.driver.find_element(By.XPATH, '//button[text()="Post"]').click()
            time.sleep(2)

    def follow(self, user_url, num_followers):
        self.driver.get(user_url)
        time.sleep(3)
        for _ in range(num_followers):
            follow_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Follow")]')
            if follow_button:
                follow_button.click()
                time.sleep(2)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    bot = Instabot('your_username', 'your_password')
    bot.login()
    # Example usage  
    bot.comment('https://www.instagram.com/p/YOUR_POST/', 'Nice post!', 5)  # Post URL  
    bot.follow('https://www.instagram.com/YOUR_TARGET_USER/', 10)  # User URL  
    bot.close()
