from selenium import webdriver
import time as tm
from bs4 import BeautifulSoup
#from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
Url = "http://221.233.24.23/eams/login.action"
InfoUrl = "http://221.233.24.23/eams/stdDetail.action"
GradeUrl = "http://221.233.24.23/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR"
user_id = "201701405"
password = "201701405"

def getInfos(user_id,password):
    driver = webdriver.PhantomJS()
    driver.get(Url)
    username = driver.find_element_by_id("username")
    passwd = driver.find_element_by_id("password")
    submit = driver.find_element_by_name("submitBtn")
    username.send_keys(user_id)
    passwd.send_keys(password)
    tm.sleep(1)
    submit.click()
    
    tm.sleep(1)


    #----开始获取个人信息-----
    driver.get(InfoUrl)
    html = driver.page_source
    # print(driver.page_source)
    soup = BeautifulSoup(html,"lxml")
    trs = soup.find_all("tr")
    #print(trs)
    infos = {}
    keys = []
    vals = []
    for tr in trs[1:-1]:
        tds = tr.find_all("td")
        if len(tds)<2:
            continue
        #print("----------------")
        key1 = tds[0].getText()[:-1]   #
        val1 = tds[1].getText()
        key2 = tds[2].getText()[:-1]
        val2 = tds[3].getText()
        keys.append(key1)
        vals.append(val1)
        keys.append(key2)
        vals.append(val2)
    for i in range(len(vals)-1):
        infos[keys[i]] = vals[i]
    #return infos
    tm.sleep(1)
   
    #infos["学号"] = infos[keys[0]]
    #infos["姓名"] = infos[keys[1]]
    #print(infos["姓名"])   
    #print(infos["学号"])
    #-----结束个人信息查询----


    driver.get(GradeUrl)
    html = driver.page_source
    
    #print(driver.page_source)
    soup = BeautifulSoup(html,"lxml")
    point = soup(class_="gridtable")
    tables = soup.find_all("table")
    #print(tables)
    #print(len(tables))
    point_trs = tables[0].find_all("tr")
    grade_trs = tables[1].find_all("tr")
    point_keys = []
    all_point_keys = ["类型","必修门数","必修总学分","必修平均绩点"]
    grade_keys = []
    points = []
    all_point = {}
    points = [] 
    grades = []
    
    
    time = point_trs[-1].getText().split("间")[1][1:].strip()
    #print(time)
    all_point_ths = point_trs[-2].find_all("th")
    
    for idx, all_point_th in enumerate(all_point_ths):
        all_point[all_point_keys[idx]] = all_point_th.getText()
    #print(all_point)
    
    for point_th in point_trs[0].find_all("th"):
        point_keys.append(point_th.getText())
    
    for grade_th in grade_trs[0].find_all("th"):
        grade_keys.append(grade_th.getText())
    #print(point_keys)
    #print(grade_keys)
    for point_tr in point_trs[1:-2]:
            point = {}      
            point_tds = point_tr.find_all("td")
            for idx,point_td in enumerate(point_tds):
                    point[point_keys[idx]] = point_td.getText()
            points.append(point)
    #print(points)
    for grades_tr in grade_trs[1:]:
            grade = {}
            grades_tds = grades_tr.find_all("td")
            for idx,grade_td in enumerate(grades_tds):
                    grade[grade_keys[idx]] = grade_td.getText().strip()
            grades.append(grade)
    print(grades)
    #print(all_point)
    infos["统计时间"] = time
    infos["绩点"] = points
    infos["总绩点"] = all_point
    infos["成绩"] = grades
    return(infos)
#getInfos(user_id,password)
#username = "201704495"
#password = "201704495"
#getInfos(username,password)

