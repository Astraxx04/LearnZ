import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options =chrome_options)

driver.get("http://127.0.0.1:5001/")

driver.maximize_window()
driver.implicitly_wait(20)

# get started button,wrong credentials enter
driver.find_element(By.XPATH, "//*[@id='header black']/div/a/ul/li").click()


print("Signing in with wrong credentials\n")
time.sleep(1)
print("USN:Wrong USN")
print("Password:Wrong Password")
driver.find_element(By.ID, "Newusn").send_keys("Wrong USN")

driver.find_element(By.ID, "Password").send_keys("randompw")
time.sleep(1)


# to avoid target out of bound error
# Get the dimensions of the current window
window_size = driver.get_window_size()
max_x = window_size['width']
max_y = window_size['height']

# Calculate the maximum x and y values that the mouse can be moved to
max_x -= 1
max_y -= 1

# Move the mouse to the maximum x and y values
ActionChains(driver).move_by_offset(max_x, max_y).perform()

# to click on login with wrong credentials
#print(driver.find_element(By.ID,"Login").is_displayed())
driver.implicitly_wait(20)
time.sleep(1)

#login click
ele=driver.find_element(By.ID, "Login")
driver.execute_script("arguments[0].click();", ele)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/button")
time.sleep(1)

# Switch to the pop-up window

output1=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]")
data1=output1.text
print("\nPop-up result:-")
if data1=="Invalid USN/Password!!" :
    print("Invalid USN/Password")

print("\nSigning up with new credentials")
#driver.find_element(By.XPATH, "//*[@id='header']/div/a/ul/li").click()
time.sleep(1)
#sign up button click
ele1=driver.find_element(By.XPATH, "//*[@id='header']/div/a/ul")
driver.execute_script("arguments[0].click();", ele1)


ele1 = driver.find_element(By.ID, "CollegeName")
drp = Select(ele1)
drp.select_by_visible_text("DSCE")


fn = ['Akash', 'Janesh','Gagan','Bhawesh','Ayushi','Nidhi','Aditi','Lakshitha','Anujna','Ahmed']
n=random.randint(0,9)

driver.find_element(By.ID,"FName").send_keys(fn[n])
time.sleep(1)

ln = ['Cena','Wayne','Kent','Allen','Kyle','Potts','Romanoff','Morgan','Stark','Ivy']
n1=random.randint(0,9)
driver.find_element(By.ID,"LName").send_keys(ln[n1])


mail=(fn[n]+"@"+ln[n1]+".com")
driver.find_element(By.ID,"email").send_keys(mail)


usn= random.randint(0,5000)
driver.find_element(By.ID,"usn").send_keys(usn)
time.sleep(1)
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

print("Sign up complete with the following credentials\nUSN: "+str(usn)+"\nPassword:"+str(pw))
time.sleep(1)
print("\nSigning in..")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/button").click()
time.sleep(1)
driver.find_element(By.ID, "Newusn").send_keys(usn)
time.sleep(1)
print("USN :"+str(usn))
driver.find_element(By.ID, "Password").send_keys(pw)
time.sleep(1)
print("Password :"+str(pw))

# login click of newly created user
ele2=driver.find_element(By.ID, "Login")
driver.execute_script("arguments[0].click();", ele2)
time.sleep(1)
# login successful pop up
output2=driver.find_element(By.XPATH,"/html/body/div/div/div[1]")
data2=output2.text

print("\nPop-up result:-")
if data2=="Login Successful!!":
    print("Login Successful")

driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/button").click()
time.sleep(1)
print("\nNavigating to Elements of Mechanical Engineering Quiz")
# hovering over js fundamentals
admin=driver.find_element(By.XPATH,"//*[@id='CourseContainer']/div[1]/div/h2")
actions=ActionChains(driver)
actions.move_to_element(admin).click().perform()
time.sleep(1)
elecont=driver.find_element(By.XPATH, "//*[@id='Elements of Mechanical Engineering']")
driver.execute_script("arguments[0].click();", elecont)
# driver.find_element(By.XPATH,"///*[@id='Basic Electrical Engineering]").click()

#Function to hover over quiz
admin1=driver.find_element(By.XPATH,"/html/body/div/div[2]/div")
actions1=ActionChains(driver)
continue1=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/a/p/button")
actions1.move_to_element(admin1).move_to_element(continue1).click().perform()
driver.find_element(By.XPATH,"/html/body/div/div/table/tbody[1]/tr/td[3]/a").click()
get_url = driver.current_url
print("The current url is:"+str(get_url))


time.sleep(1)


