from splinter.browser import Browser
import time
import sys
from threading import Thread


def AutoInfo(driver):
    
    #name
    driver.execute_script("document.getElementById('order_billing_name').value='*Name*'")

    #email
    driver.execute_script("document.getElementById('order_email').value='*email*'")

    #Tel
    driver.execute_script("document.getElementById('order_tel').value='*tel*'")
     




def AutoAddress(driver):
    #Street name
    driver.execute_script("document.getElementById('bo').value='*Street Name*'")

    #apt number
    driver.execute_script("document.getElementById('oba3').value='*Apt Number*'")

    #zip
    driver.execute_script("document.getElementById('order_billing_zip').value='*Zip code*'")

    #city
    driver.execute_script("document.getElementById('order_billing_city').value='*city*'")


 


def AutoCardInfoOne(driver):

    #State
    driver.find_by_value("MA").click()
  

    #Country
    driver.find_by_value('USA').click()
    
    
    #credit card number
    driver.execute_script("document.getElementById('nnaerb').value='12345678'")

    #expiration month
    driver.find_by_value("01").click()
 



 

def AutoCardInfoTwo(driver):
   
   #expiration year
    driver.find_by_value("2020").click()
    
    #CVV
    driver.execute_script("document.getElementById('orcer').value='123'")
    driver.find_by_css('label.terms').click()


def supreme(url, keyword, color):

# all are strings ''
    b = Browser(driver_name = "chrome")
    input("Press Enter to continue...")
    b.visit(url)
    b.find_link_by_partial_text(keyword).click()
    #choose color
    if color == 'Black':
        b.find_by_xpath("/html/body//a[@data-style-name='Black']").click()
    elif color == 'Red':
        b.find_by_xpath("/html/body//a[@data-style-name='Red']").click()
    elif color == 'Blue':
        b.find_by_xpath("/html/body//a[@data-style-name='Blue]").click()
    elif color == 'Navy':
        b.find_by_xpath("/html/body//a[@data-style-name='Navy]").click()
    elif color == 'Green':
        b.find_by_xpath("/html/body//a[@data-style-name='Green']").click()
        
    while True:
        elementList = b.find_by_value("add to cart")
        if not elementList.is_empty():
            break
    b.find_by_value("add to cart").click()
 

    while True:
        elementList = b.find_link_by_href("https://www.supremenewyork.com/checkout")
        if not elementList.is_empty():
            break
    b.find_link_by_href("https://www.supremenewyork.com/checkout").click()

    while True:
        elementList = b.find_by_value('USA')
        if not elementList.is_empty():
            break

    threads = []
    t_1 = Thread(target = AutoInfo, args = [b])
    t_1.start()
    threads.append(t_1)
    
    t_2 = Thread(target = AutoAddress, args = [b])
    t_2.start()
    threads.append(t_2)
    
    t_3= Thread(target = AutoCardInfoOne, args = [b])
    t_3.start()
    threads.append(t_3)
    
    t_4= Thread(target = AutoCardInfoTwo, args = [b])
    t_4.start()
    threads.append(t_4)  



if __name__ == "__main__":
    supreme("https://www.supremenewyork.com/shop/all/jackets",'Leather Trucker Jacket', 'Black')




####################JWingD#########################
