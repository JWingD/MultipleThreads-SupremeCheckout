from splinter.browser import Browser
import time
import sys
from threading import Thread

def supreme(url, keyword, color):

# all are strings ''
    b = Browser(driver_name = "chrome")
    b.visit(url)
    button_type = b.find_link_by_partial_text(keyword)
    button_type.click()
    time.sleep(2)
    #choose color
    if color == 'Black':
        button_color=b.find_by_xpath("/html/body//a[@data-style-name='Black']")
        button_color.click()
    elif color == 'Red':
        button_color=b.find_by_xpath("/html/body//a[@data-style-name='Red']")
        button_color.click()
    elif color == 'Blue':
        button_color=b.find_by_xpath("/html/body//a[@data-style-name='Blue']")
        button_color.click()
    elif color == 'Navy':
        button_color=b.find_by_xpath("/html/body//a[@data-style-name='Navy']")
        button_color.click()
    elif color == 'Green':
        button_color=b.find_by_xpath("/html/body//a[@data-style-name='Green']")
        button_color.click()
        
    time.sleep(2)
    button_cart = b.find_by_value("add to cart")
    button_cart.click()

    time.sleep(2)
    #b.is_element_visible_by_href("https://www.supremenewyork.com/checkout")
    #b.implicitly_wait(5)
    button_checkout = b.find_link_by_href("https://www.supremenewyork.com/checkout")
    button_checkout.click()

        #Auto Filling
    #time.sleep(10)

        #Name: First and Last
    b.execute_script("document.getElementById('order_billing_name').value='Martino Last Name'")

        #email
    b.execute_script("document.getElementById('order_email').value='Martino@email.address'")

        #Tel
    b.execute_script("document.getElementById('order_tel').value='xxx-xxx-xxxx'")

        #Street name
    b.execute_script("document.getElementById('bo').value='Street Address'")

    #apt number
    b.execute_script("document.getElementById('oba3').value='Apt number'")

        #zip
    b.execute_script("document.getElementById('order_billing_zip').value='zip code'")

        #city
    b.execute_script("document.getElementById('order_billing_city').value='City'")

        #State
    button_state = b.find_by_value("MA")
    button_state.click()

        #Country
    button_country = b.find_by_value('USA')
    button_country.click()


        #credit card number
    b.execute_script("document.getElementById('nnaerb').value='123456789'")

        #expiration month
    button_month = b.find_by_value("01")
    button_month.click()

        #expiration year
    button_year = b.find_by_value("2020")
    button_month.click()

    #CVV
    b.execute_script("document.getElementById('orcer').value='123'")
    b.find_by_css('label.terms').click()



if __name__ == "__main__":
    data = [["https://www.supremenewyork.com/shop/all/jackets",'Leather Trucker','Red'],\
           ["https://www.supremenewyork.com/shop/all/shirts",'Pin Tuck', 'Black']]
    threads = [] 
    for i in range(len(data)): 
        t = Thread(target=supreme,args=data[i])
        threads.append(t) 
 
  # start all the thread
    for thr in threads:
        thr.start()
# MultipleThreads-SupremeCheckout
