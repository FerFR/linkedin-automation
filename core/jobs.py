import datetime
from .models import Post, Linkedin_Account
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from os.path import abspath
from time import sleep
import shutil


def post_in_linkedin():
    today = datetime.date.today()
    now = datetime.datetime.now()
    hours = now.hour
    if len(hours) == 1:
        hours = f'{hours}0'
    
    posts = Post.objects.filter(date=today)
    for post in posts:
        if str(post.hours).split(':')[0] == str(hours):
            user = Linkedin_Account.objects.first()
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
            driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
            driver.find_element_by_xpath('//*[@id="username"]').send_keys(user.email)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(user.password)
            driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
            driver.implicitly_wait(5)
            driver.find_element_by_xpath("//* [text() = 'Começar publicação']").click()
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/span[1]/button/li-icon').click()
            driver.find_element_by_xpath('//*[@id="image-sharing-detour-container__file-input"]').send_keys(abspath(str(post.photo)))
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/button').click()
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]').click()
            ActionChains(driver).send_keys(post.text).perform()
            driver.implicitly_wait(1)
            driver.find_element_by_xpath('//*[contains(@class, "share-box_actions")]/button').click()
            sleep(5)
            post.delete()
            driver.close()

def clear_photos():
    yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
    yesterday = yesterday.strftime('%d-%m-%y')
    shutil.rmtree(abspath(f'uploads/{yesterday}'), ignore_errors=True)

