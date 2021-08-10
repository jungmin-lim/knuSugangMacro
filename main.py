from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

import time

'''
from captcha_solver import CaptchaSolver
import urllib.request
import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
'''

def get_login_info():

    f = open('login_info.txt', 'r')
    info = f.readline()
    info = info.rstrip()
    infos = info.split(',')

    return infos[0], infos[1], infos[2]


driver = Chrome()
stu_nbr, usr_id, passwd = get_login_info()

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
    time.sleep(1)
    
    # apply session
    while driver.current_url == "https://sugang.knu.ac.kr/Sugang/cour/lectReq/onlineLectReq/list.action":
        # lecture search
        '''
        search_box = driver.find_element_by_class_name("search_box3")
        lect_code = search_box.find_element_by_id("search_subj_class_cde")
        captcha_code = search_box.find_element_by_id("captcha_cde")
        captcha_img = search_box.find_element_by_id("captcha")
        src = captcha_img.get_attribute("src")

        urllib.request.urlretrieve(src, "captcha.png")
        im_gray = cv2.imread('captcha.png', cv2.IMREAD_GRAYSCALE)
        (thresh, im_bw) = cv2.threshold(im_gray, 127, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
        captcha_str = pytesseract.image_to_string(im_bw, lang='eng', config="--psm 8 --oem 3")
        print(captcha_str)
        captcha_code.send_keys(captcha_str)
        time.sleep(2)
        '''

        # sugang pack
        lect_pack = driver.find_element_by_id("lectPackReqGrid")
        lect_pack_list = lect_pack.find_elements_by_tag_name("tr")

        for x in lect_pack_list[2:]:
            lect_name = x.find_element_by_class_name("subj_nm")
            lect_quota = x.find_element_by_class_name("lect_quota")
            lect_req_cnt = x.find_element_by_class_name("lect_req_cnt")
            apply_button = x.find_element_by_class_name("button")
            print("%s %s/%s" %(lect_name.text, lect_quota.text, lect_req_cnt.text))

            if lect_quota.text != lect_req_cnt.text:
                print(lect_quota.text)
                print(lect_req_cnt.text)
                apply_button.click()
                driver.implicitly_wait(10)
                alert = Alert(driver)
                print(alert.get_Text())
                alert.accept()

            else:
                print("lecture full")

        time.sleep(1)
        driver.refresh()
        driver.implicitly_wait(300)
