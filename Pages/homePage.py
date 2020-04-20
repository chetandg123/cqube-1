from selenium.webdriver import ActionChains
import time

from selenium.webdriver.support.select import Select

from Locators.locators import Locators
class HomePage():
    def __init__(self,driver):
        self.driver=driver
        self.Points = Locators.points
        self.Blocks = Locators.blocks
        self.Cluster = Locators.cluster
        self.Schools = Locators.schools
        self.HomeButton = Locators.homebutton
        self.select_districts = Locators.select_district
        self.select_blocks = Locators.select_blocks
        self.select_clusters = Locators.select_clusters



    def MouseOverOnPoints(self):
        list=self.driver.find_elements_by_class_name(self.Points)
        def mouseover(i):
            action = ActionChains(self.driver)
            action.move_to_element(list[i]).perform()
            time.sleep(5)
            del action
        i = 0
        while i < len(list):
            mouseover(i)
            i = i + 1

    def ClickOn_Blocks(self):
        self.driver.find_element_by_xpath(self.Blocks).click()
    def ClickOn_Cluster(self):
        self.driver.find_element_by_xpath(self.Cluster).click()
    def ClickOn_Schools(self):
        self.driver.find_element_by_xpath(self.Schools).click()
        
    def ClickOn_HomeButton(self):
        self.driver.find_element_by_id(self.HomeButton).click()
        def select_district_block_cluster(self):
        select_district = Select(self.driver.find_element_by_xpath(self.select_districts))
        select_block = Select(self.driver.find_element_by_xpath(self.select_blocks))
        select_cluster = Select(self.driver.find_element_by_xpath(self.select_clusters))
        time.sleep(5)
        for x in range(1, len(select_district.options)):
            select_district.select_by_index(x)
            time.sleep(2)
            for y in range(1, len(select_block.options)):
                select_block.select_by_index(y)
                time.sleep(2)
                for z in range(1, len(select_cluster.options)):
                    select_cluster.select_by_index(z)
                    time.sleep(2)
                    self.MouseOverOnPoints()

