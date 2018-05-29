from framework.base_page import BasePage

class SportNewsHomePage(BasePage):
    #NBA入口
    nba_link = "xpath=>//*[@id='col_nba']/div[2]/ul[1]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
        self.sleep(2)