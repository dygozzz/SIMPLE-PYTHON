from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.ibm.com/br-pt")

# Capture um screenshot da página
driver.save_screenshot("pagina.png")

driver.quit()
