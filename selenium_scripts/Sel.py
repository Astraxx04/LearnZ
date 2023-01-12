import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
serv_obj=Service()


driver= webdriver.Chrome(service =serv_obj)
driver.maximize_window()
driver.implicitly_wait(20)

#teacher login
driver.get("http://127.0.0.1:5001/student_signin")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='sign-in-form']/div[3]/a").click()
time.sleep(1)
driver.find_element(By.ID,"Newteachid").send_keys("t1")
time.sleep(1)
driver.find_element(By.ID,"Password").send_keys("123")
time.sleep(1)
driver.find_element(By.ID,"Login").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='Elements of Mechanical Engineering']").click()
time.sleep(1)

admin4=driver.find_element(By.XPATH,"/html/body/div/div[1]/div")
usermgt4=driver.find_element(By.XPATH,"//*[@id='card_quiz']/div/div/a/p/button")
actions3=ActionChains(driver)
time.sleep(1)
actions3.move_to_element(admin4).move_to_element(usermgt4).click().perform()
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='id_quiz_name']").send_keys("Power Transmission")
time.sleep(1)
driver.find_element(By.XPATH,"//*[@id='id_link']").send_keys("https://forms.gle/ZytoBbTHhcrD4nZS6")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div/form/button").click()
time.sleep(3)


driver.get("http://127.0.0.1:5001/")
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='header black']/div/a/ul/li").click()
time.sleep(1)
driver.find_element(By.ID, "Newusn").send_keys("Wrong USN")
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys("randompw")
time.sleep(1)
driver.find_element(By.ID, "Login").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/button").click()
time.sleep(1)
#driver.find_element(By.XPATH, "//*[@id='header']/div/a/ul/li").click()
#time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='header']/div/a/ul").click()
time.sleep(1)

ele1 = driver.find_element(By.ID, "CollegeName")
drp = Select(ele1)
drp.select_by_visible_text("DSCE")

fn = ['Akash', 'Janesh','Gagan','Bhawesh','Ayushi','Nidhi','Aditi','Lakshitha','Anujna','Ahmed']
n=random.randint(0,9)

driver.find_element(By.ID,"FName").send_keys(fn[n])

ln = ['Cena','Wayne','Kent','Allen','Kyle','Potts','Romanoff','Morgan','Stark','Ivy']
n1=random.randint(0,9)
driver.find_element(By.ID,"LName").send_keys(ln[n1])

mail=(fn[n]+"@"+ln[n1]+".com")
driver.find_element(By.ID,"email").send_keys(mail)

usn= random.randint(0,5000)
driver.find_element(By.ID,"usn").send_keys(usn)
pw=random.randint(0,15000)
driver.find_element(By.ID,"password").send_keys(pw)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(1)

#var= driver.find_element(By.XPATH, "//*[@id='SignUpBtn']")
#driver.execute_script("arguments[0].scrollIntoView();",var)

#driver.implicitly_wait(20)


driver.find_element(By.ID,"ConfiPass").send_keys(pw)
time.sleep(1)

driver.find_element(By.ID,"SignUpBtn").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/button").click()
time.sleep(1)
driver.find_element(By.ID, "Newusn").send_keys(usn)
time.sleep(1)
driver.find_element(By.ID, "Password").send_keys(pw)
time.sleep(1)
driver.find_element(By.ID, "Login").click()
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/button").click()
time.sleep(1)

#hovering over mechanical eng.
admin1=driver.find_element(By.XPATH,"//*[@id='CourseContainer']/div[2]/div/h2")
usermgt1=driver.find_element(By.ID,"Elements of Mechanical Engineering")
actions1=ActionChains(driver)
actions1.move_to_element(admin1).move_to_element(usermgt1).click().perform()
time.sleep(1)

admin5=driver.find_element(By.XPATH,"/html/body/div/div[2]/div")
usermgt5=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/a/p/button")
actions5=ActionChains(driver)
actions5.move_to_element(admin5).move_to_element(usermgt5).click().perform()

driver.find_element(By.XPATH,"/html/body/div/div/table/tbody[1]/tr/td[3]/a").click()
time.sleep(6)