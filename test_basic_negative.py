def test_browser():

    """ 
    Test case TLP-1: Open url testqastudio.me
    """
    chrome_options = Options()
    chrome_options.add_argument("start-maximized") # открываем на полный экран
    chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
    chrome_options.add_argument("--disable-extensions") # отключаем расширения
    
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
		
    url = "https://testqastudio.me/"
    driver.get(url=url)
		# ищем по селектору элемент меню "Бестселлеры" и кликаем по нему
    element = driver.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']")
    element.click()
		# ищем по селектору карточку "ДИВВИНА Журнальный столик" и кликаем по нему,
    # чтобы просмотреть детали
    element = driver.find_element(by=By.CSS_SELECTOR, value='[class*="post-11340"]')
    element.click()
		# ищем по имени класса артикул для "Журнального столика"
    sku = driver.find_element(By.CLASS_NAME, value="sku")
		# проверяем соответствие
    assert sku.text == 'BFB9ZOK211', "Unexpected sku"
    
    
