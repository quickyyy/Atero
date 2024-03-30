import os

import undetected_chromedriver as uc
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import random
import configparser

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Logger:
    def log_message(self, message=None):
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f'[{current_time}] {Fore.LIGHTBLACK_EX}{message}{Style.RESET_ALL}')

    def test_log(self, function_name=None, message=None):
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f'[{current_time}] [TEST] [{function_name}] {message}')

    def sleep_log(self, seconds):
        time.sleep(seconds)


options = uc.ChromeOptions()
log = Logger()
config = configparser.ConfigParser()

def bot_connect(driver):
    log.log_message('Bot connect function loading')
    # log.log_message('Trying to load while True')
    while True:
        try:
            # log.log_message('Trying to load Try')
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@class="extend"]/button[@class="btn btn-tiny btn-success server-extend-end"]'))
            )
            button.click()
            log.log_message(f'{Fore.GREEN}Prodlil{Style.RESET_ALL}')
        except KeyboardInterrupt:
            log.log_message('Got ctrl+c')
            driver.quit()
            driver.close()
        except:
            timer = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="read-our-tos"]/main/section/div[3]/div[2]/div[1]/div/div/div[1]/div[1]/div'))
            ).text
            # log.log_message('Cannot click on button')
            log.log_message(f'Timer is: {Fore.LIGHTGREEN_EX}{timer}{Style.RESET_ALL}')
            fuckad(driver)
            log.sleep_log(random.randint(1, 7))
            pass


def fuckad(driver):
    try:
        # log.log_message(message='Trying to load fuckad')
        button = driver.find_element(By.XPATH,
                                     '//div[contains(text(), "Всё равно продолжить с блокировщиком рекламы")]')
        button.click()

        log.sleep_log(4)
        return True
    except:
        # log.log_message('Error in fuckad')
        return False


def printlogo():
    logo = """
 $$$$$$\    $$\                                   
$$  __$$\   $$ |                                  
$$ /  $$ |$$$$$$\    $$$$$$\   $$$$$$\   $$$$$$\  
$$$$$$$$ |\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ 
$$  __$$ |  $$ |    $$$$$$$$ |$$ |  \__|$$ /  $$ |
$$ |  $$ |  $$ |$$\ $$   ____|$$ |      $$ |  $$ |
$$ |  $$ |  \$$$$  |\$$$$$$$\ $$ |      \$$$$$$  |
\__|  \__|   \____/  \_______|\__|       \______/ 
    """
    lines = logo.split('n')

    for line in lines:
        print(line)
        time.sleep(0.2)


def loadserver(session_cookie, server_id, server_ip):
    try:
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument("start-maximized")
        user_agent_str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        options.add_argument(f"--user-agent={user_agent_str}")
        log.log_message('Writed options.')
        driver = uc.Chrome( options=options)
        log.log_message(message='Opened driver.')
        log.sleep_log(3)
        driver.get('https://aternos.org/servers/')
        log.log_message(message='Initializing...')
        # log.sleep_log(3)
        driver.add_cookie(
            {
                'name': 'ATERNOS_SESSION',
                'value': session_cookie
            }
        )
        driver.add_cookie(
            {
                'name': "ATERNOS_SERVER",
                'value': server_id
            }
        )
        log.sleep_log(1)
        driver.get('https://aternos.org/server/')
        log.log_message('Going to https://aternos.org/server/')
        log.sleep_log(1)
        driver.refresh()
        # log.sleep_log(5)
        fuckad(driver)
        # log.sleep_log(3)
        driver.refresh()
        # log.sleep_log(5)
        fuckad(driver)
        log.sleep_log(3)
        element = driver.find_element(By.XPATH,
                                      '//*[@id="read-our-tos"]/main/section/div[3]/div[2]/div[1]/div/span[1]/span')
        # log.sleep_log(3)
        if "Оффлайн" in element.text:
            log.log_message(f'Server is {Fore.LIGHTRED_EX}offline!{Style.RESET_ALL} Trying to turn it on.')
            log.sleep_log(3)
            driver.find_element(By.XPATH, '//*[@id="start"]').click()
            log.log_message(f'Server is {Fore.LIGHTYELLOW_EX}loading{Style.RESET_ALL}...')
        if 'Запуск' in element.text:
            log.sleep_log(3)
            log.log_message(f'Server is {Fore.LIGHTYELLOW_EX}loading{Style.RESET_ALL}, waiting')
            log.sleep_log(35)
            element = driver.find_element(By.XPATH,
                                          '//*[@id="read-our-tos"]/main/section/div[3]/div[2]/div[1]/div/span[1]/span').text
            if 'Онлайн' in element.text:
                log.sleep_log(3)
                log.log_message(f'Server is {Fore.LIGHTGREEN_EX}online{Style.RESET_ALL} cool!')
                bot_connect(driver)
        if 'Онлайн' in element.text:
            log.sleep_log(3)
            log.log_message(
                f'Server is {Fore.LIGHTGREEN_EX}online{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}cool!{Style.RESET_ALL}')
            bot_connect(driver)
    except KeyboardInterrupt as e:
        log.log_message(f'{Fore.RED}CTRL+C pressed, closing driver...{Style.RESET_ALL}')
        driver.quit()
        driver.close()
    except Exception as e:
        log.log_message(f'Error:  {e}')
        driver.quit()
        driver.close()

if __name__ == '__main__':
    os.system('cls')
    printlogo()
    log.log_message(f'{Fore.WHITE}Atero{Style.RESET_ALL} - a script to automatically load a server on aternos and keep it online')
    log.log_message(f'Telegram Blog - {Fore.WHITE}https://t.me/bredcookie{Style.RESET_ALL}')
    log.log_message(f'Github repository - {Fore.WHITE}https://github.com/quickyyy/Atero{Style.RESET_ALL}')
    config.read('config.ini')
    ip = config['aternos.server']['ip']
    server_id = config['aternos.server']['server_id']
    session_cookie = config['aternos.server']['session_cookie']
    log.log_message(f'Got ip: {Fore.WHITE}{ip}{Style.RESET_ALL}')
    log.log_message(f'Got server_id: {Fore.WHITE}{server_id}{Style.RESET_ALL}')
    log.log_message(f'Got session_cookie: {Fore.WHITE}{session_cookie}{Style.RESET_ALL}')
    loadserver(session_cookie, server_id, ip)
