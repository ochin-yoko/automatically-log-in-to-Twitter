from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
USERNAME = 'USERNAME'
PASSWORD = 'PASSWORD'
MAILADDRESS = 'MAILADDRESS'
driver = webdriver.Chrome('PATH of Chromedriver.exe')
error_flg = False
target_url = 'https://twitter.com/i/flow/login'
driver.get(target_url)  
sleep(3)

def email_Input():
    driver.find_element(By.NAME,"text").send_keys(MAILADDRESS)
def username_Input():
    try:
        driver.find_element(By.NAME,"text").send_keys(USERNAME)
    except:
        driver.find_element(By.NAME,"username").send_keys(USERNAME)
def next_Click():
    try:
        driver.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]").click()
    except:
        driver.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div").click()
def password_Input():
    driver.find_element(By.NAME,"password").send_keys(PASSWORD)
def login_Click():
    driver.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div").click()

try:
    #ユーザー名入力
    username_Input()
    #次へボタン押下
    next_Click()
    sleep(1)

    #「電話番号またはメールアドレスを確認してください」が表示されたら
    try:
        #メアド入力
        email_Input()
        #次へボタン押下
        next_Click()
        sleep(1)
        #パスワード入力
        password_Input()
        #ログインボタン押下
        login_Click()
        sleep(1)

    #「電話番号またはメールアドレスを確認してください」が表示されなかったら
    except:
        #パスワード入力
        password_Input()
        #ログインボタン押下
        login_Click()
        sleep(1)

        #「アカウントの安全のために」が表示されたら
        try:
            #メアドに認証の実装はめんどいので一旦パス
            address_Certification()
        #本来は例外処理を書くが現在はtryで必ず例外を吐くのでスルーさせる
        except:
            pass


except Exception:
    #ユーザー名入力の前に「始める前にまず電話番号、メールアドレス、またはユーザー名を入力してください」と表示されたら
    try:
        #ユーザー名入力
        username_Input()
        #次へボタン押下
        next_Click()
        sleep(1)
        #パスワード入力
        password_Input()
        #ログインボタン押下
        login_Click()
        sleep(1)
    except:
        pass
    error_flg = True
    print('ログインボタン押下時にエラーが発生しました。')

#botじゃないかの確認が出たら
try:
    driver.find_element(By.CSS_SELECTOR,".Button.EdgeButton.EdgeButton--primary").click()
    sleep(10)
    driver.find_element(By.CSS_SELECTOR,".Button.EdgeButton.EdgeButton--primary").click()
except:
    pass

#twitterを始めるみたいなバナーが出てきたら
try:
    driver.find_element(By.CSS_SELECTOR,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div').click()
except:
    pass