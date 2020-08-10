from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


def get_login_info():

    f = open('login_info.txt', 'r')
    info = f.readline()
    info = info.rstrip()
    infos = info.split(',')

    return infos[0], infos[1], infos[2]


driver = Chrome()
stu_nbr, usr_id, passwd = get_login_info()
i = 1

# open chrome window ("url")
driver.get("http://sugang.knu.ac.kr")

while True:
    # login session
    login_box = driver.find_element_by_id("loginForm")
    stu_nbr_box = login_box.find_element_by_id("user.stu_nbr")
    usr_id_box = login_box.find_element_by_id("user.usr_id")
    passwd_box = login_box.find_element_by_id("user.passwd")
    submit = login_box.find_element_by_class_name("login")

    stu_nbr_box.send_keys(stu_nbr)
    usr_id_box.send_keys(usr_id)
    passwd_box.send_keys(passwd)
    submit.click()

    apply_button = driver.find_element_by_xpath("//*[@id=\"lectPackReqGrid_0\"]/td[11]")

    apply_button.click()
    alert = driver.switch_to.alert()
    print(driver.switch_to.alert.get_Text())
    alert.accept()

    # apply session
    while driver.current_url == "https://sugang.knu.ac.kr/Sugang/cour/lectReq/onlineLectReq/list.action":

        lect_quota = driver.find_element_by_xpath("//*[@id=\"lectPackReqGrid_0\"]/td[8]")
        lect_req_cnt = driver.find_element_by_xpath("//*[@id=\"lectPackReqGrid_0\"]/td[9]")
        apply_button = driver.find_element_by_xpath("//*[@id=\"lectPackReqGrid_0\"]/td[11]")

        if lect_quota.text != lect_req_cnt.text:
            apply_button.click()
            alert = driver.switch_to.alert()
            print(alert.get_Text())
            alert.accept()

        else:
            print("lecture full")

        driver.refresh()
        time.sleep(2)
