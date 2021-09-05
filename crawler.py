from tqdm import trange
from selenium import webdriver
import time


def main():
    with open('maple_name.txt', 'w', encoding='utf-8') as f:
        driver = webdriver.Chrome('./chromedriver')
        driver.implicitly_wait(1)
        for page in trange(1, 10): ## page number
            driver.get(f"https://maplestory.nexon.com/Ranking/World/Total?page={page}")
            for i in range(1, 11):
                temp = driver.find_element_by_xpath(
                    f'//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr[{i}]/td[2]/dl/dt/a')
                f.write(temp.text + '\n')
            time.sleep(0.1)


if __name__ == '__main__':
    main()
