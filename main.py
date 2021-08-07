from selenium import webdriver
import time

chrome_driver_path = "/Users/nadun/chrome-web-driver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.speedtest.net/result/11844637854")

time.sleep(2)
go_button = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
go_button.click()
time.sleep(45)
download_speed_obj = driver.find_element_by_xpath(
    '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
download_speed = download_speed_obj.text

# twitter bot
driver.get("https://twitter.com/SriLankaTelecom")
time.sleep(2)
twitter_login = driver.find_element_by_xpath('//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/a')
twitter_login.click()
time.sleep(2)
user_name = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
user_name.send_keys('nissanka_nadun')
time.sleep(1)
password = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys('nadun123')
login_button = driver.find_element_by_xpath(
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
login_button.click()
tweet_btn = driver.find_element_by_css_selector(".css-1dbjc4n ")
tweet_btn.click()
# tweet here
