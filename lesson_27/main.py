from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://www.python.org/"

driver = webdriver.Chrome()
driver.get(URL)

stored_events = {}
# event1_year = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time/span').text
# event1_date = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time').text

counter = 1
for i in range(0, 5):
    time_url = f"#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child({counter}) > time"
    event_url = f"#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li:nth-child({counter}) > a"
    events_time = driver.find_element(By.CSS_SELECTOR, value=time_url)
    event_time = events_time.get_attribute("datetime").split("T")[0]
    print(event_time) #event1_year., event1_date

    events = driver.find_element(By.CSS_SELECTOR, value=event_url)
    event = events.text
    print(event) #event1_year., event1_date
    
    stored_events[i] = {"time": event_time, "name": event}

    # stored_events[i]["time"] = event_time
    # stored_events[i]["name"] = event
    counter += 1
print(stored_events)