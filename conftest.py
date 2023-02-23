import pytest

from selenium import webdriver



@pytest.fixture
def chrom_options():
    chrom_options = webdriver.ChromeOptions()
    chrom_options.add_argument('--kiosk')
    chrom_options.add_argument("--window-size=1400,800")
    return chrom_options

@pytest.fixture(scope = 'class', autouse = True)
def browser(): # подключаем драйвер Chrome и открываем веб-стрницу
    driver = webdriver.Chrome(executable_path = 'chromedriver.exe')
    yield driver
    driver.quit()
