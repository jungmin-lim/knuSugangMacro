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


    # apply session
    while driver.current_url == "https://sugang.knu.ac.kr/Sugang/cour/lectReq/onlineLectReq/list.action":

        lect_pack = driver.find_element_by_id("lectPackReqGrid")
        lect_pack_0 = lect_pack.find_element_by_id("lectPackReqGrid_0")
        lect_pack_1 = lect_pack.find_element_by_id("lectPackReqGrid_1")
        lect_pack_2 = lect_pack.find_element_by_id("lectPackReqGrid_2")
        lect_pack_list = [lect_pack_0, lect_pack_1, lect_pack_2]

        for x in lect_pack_list:
            lect_name = x.find_element_by_class_name("subj_nm")
            lect_quota = x.find_element_by_class_name("lect_quota")
            lect_req_cnt = x.find_element_by_class_name("lect_req_cnt")
            apply_button = x.find_element_by_class_name("button")
            print("%s %s/%s" %(lect_name.text, lect_quota.text, lect_req_cnt.text))

            if lect_quota.text != lect_req_cnt.text:
                print(lect_quota.text)
                print(lect_req_cnt.text)
                # apply_button.click()
                alert = driver.switch_to.alert()
                print(alert.get_Text())
                alert.accept()

            else:
                print("lecture full")

        driver.refresh()
        time.sleep(2)
