from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Enter Web Site URL like( https://sahildholpuria.tech/ ) to Get HTML Source Code. \n")
WebName = str(input("Enter URL here : "))

browser = webdriver.Chrome(executable_path="./drivers\chromedriver.exe")
browser.get(WebName)

f = open('./WebSourceCode.txt','w')
f.write(browser.page_source)

browser.close()
