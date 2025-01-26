class base_page():
    base_url = 'http://120.26.37.204:8081'

    def __init__(self,driver):
        self.driver=driver


    def bp_find_element(self,*loc):
        return self.driver.find_element(*loc)

    def bp_find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def open(self,url):
        print(self,url)
        self.driver.get(self.base_url+url)