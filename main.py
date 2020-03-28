from selenium import webdriver as wb
import selenium
from selenium.webdriver.common.keys import Keys as k
import time

d = wb.Chrome()

date = '2020-01-04'  # input('date(eg.2017-07-17):')

#   [[introduction of words]]:
#    train   ================>  direction
#           |___________|______________..._____________|______________|
#       whole_beg    mid_beg                        mid_beg         whole_end

whole_beg = '长沙'  # input('whole_beg:')
whole_end = '虎门'  # input('whole_end:')

mid_beg = '株洲'  # input('mid_beg:')
mid_end = '广州'  # input('mid_end:')

d.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=&ts=&date=' + date + '&flag=N,Y,Y')

whole_trains = []
while True:
    try:
        d.find_element_by_css_selector('#fromStationText').click()
        d.find_element_by_css_selector('#fromStationText').send_keys(whole_beg)
        d.find_element_by_css_selector('#fromStationText').send_keys(k.ENTER)

        d.find_element_by_css_selector('#toStationText').click()
        d.find_element_by_css_selector('#toStationText').send_keys(whole_end)
        d.find_element_by_css_selector('#toStationText').send_keys(k.ARROW_DOWN)
        d.find_element_by_css_selector('#toStationText').send_keys(k.ARROW_DOWN)
        d.find_element_by_css_selector('#toStationText').send_keys(k.ENTER)

        time.sleep(0.2)
        d.find_element_by_css_selector('#query_ticket').click()

        while not whole_trains:
            time.sleep(0.1)
            whole_trains = d.find_elements_by_css_selector('.number')
        break
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(0.1)
        continue

for i in range(len(whole_trains)):
    whole_trains[i] = whole_trains[i].text

time.sleep(1)

beg_trains = []
while True:
    try:
        d.find_element_by_css_selector('#fromStationText').click()
        d.find_element_by_css_selector('#fromStationText').send_keys(whole_beg)
        d.find_element_by_css_selector('#fromStationText').send_keys(k.ENTER)

        d.find_element_by_css_selector('#toStationText').click()
        d.find_element_by_css_selector('#toStationText').send_keys(mid_beg)
        d.find_element_by_css_selector('#toStationText').send_keys(k.ENTER)

        time.sleep(0.2)
        d.find_element_by_css_selector('#query_ticket').click()

        while not beg_trains:
            time.sleep(0.1)
            beg_trains = d.find_elements_by_css_selector('.number')
        break
    except selenium.common.exceptions.ElementClickInterceptedException:
        time.sleep(0.1)
        continue

for i in range(len(beg_trains)):
    beg_trains[i] = beg_trains[i].text

valid_trains = []
for i in whole_trains:
    for j in beg_trains:
        if i == j:
            valid_trains.append(i)

ans = input('Do you want to query for end meets?(yes for 1) Only owning ID card and passport can this be feasible.')
if ans == '1':

    end_trains = []
    while True:
        try:
            d.find_element_by_css_selector('#fromStationText').click()
            d.find_element_by_css_selector('#fromStationText').send_keys(mid_end)
            d.find_element_by_css_selector('#fromStationText').send_keys(k.ENTER)

            d.find_element_by_css_selector('#toStationText').click()
            d.find_element_by_css_selector('#toStationText').send_keys(whole_end)
            d.find_element_by_css_selector('#toStationText').send_keys(k.ENTER)

            d.find_element_by_css_selector('#query_ticket').click()

            while not end_trains:
                time.sleep(0.1)
                end_trains = d.find_elements_by_css_selector('.number')
            break
        except selenium.common.exceptions.ElementClickInterceptedException:
            time.sleep(0.1)
            continue

    final_trains = []
    for i in valid_trains:
        for j in end_trains:
            if i == j.text:
                final_trains.append(i)
    print(final_trains)

else:
    print(valid_trains)

d.close()
