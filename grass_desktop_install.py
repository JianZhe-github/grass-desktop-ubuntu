from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from fnmatch import filter
from pyvirtualdisplay import Display
import time
import sys
import os
import subprocess

# 标志文件路径
flag_file = "/root/grass_install_done.flag"

# 如果标志文件存在，退出脚本
if os.path.exists(flag_file):
    print("Python script has already been executed, exiting.")
else:
    # 启动虚拟显示
    display = Display(visible=0, size=(1024, 768))
    display.start()

# 从环境变量中获取用户名和密码
env_email = os.environ.get('email')
env_password = os.environ.get('password')

# 配置Firefox
options = Options()
# options.add_argument("--headless")  # 如需无头模式，可取消注释
service = Service("/usr/local/bin/geckodriver")

# 登入页面URL
login_url = 'https://app.getgrass.io/'
# 目标页面URL
target_url = 'https://app.getgrass.io/dashboard'

# 初始化Firefox WebDriver
driver = webdriver.Firefox(service=service, options=options)

try:
    # 打开登录页面
    driver.get(login_url)
    
    # 等待页面加载
    time.sleep(5)

    # 输入用户名和密码
    driver.find_element(By.NAME, 'user').send_keys(env_email)
    driver.find_element(By.NAME, 'password').send_keys(env_password)

    # 提交表单
    driver.find_element(By.NAME, 'password').submit()
    print("Login attempted")

    # 等待页面跳转
    time.sleep(3)

    # 检查是否成功登录
    if driver.current_url == target_url:
        print("Login Success")
        
        # 如果标志文件存在，退出脚本
        if os.path.exists(flag_file):
            exit(0)

        # 导航到目标页面并点击下载按钮
        driver.get('https://app.getgrass.io/dashboard/store/item/desktop')
        time.sleep(2)

        download_button = driver.find_element(By.XPATH, "//button[contains(@class, 'chakra-button') and .//p[text()='DOWNLOAD']]")
        download_button.click()
        print("Download initiated")

        # 等待下载完成
        time.sleep(7)

        # 跳转回到目标页面
        driver.get(target_url)
        time.sleep(2)

        # 定义下载目录和文件模式
        download_directory = '/root/Downloads'
        deb_file_pattern = 'grass_*.deb' 
        
        # 查找下载的文件并安装
        files = filter(os.listdir(download_directory), deb_file_pattern)
        
        for file in files:
            file_path = os.path.join(download_directory, file)  
            try:
                command = ['gdebi', '--non-interactive', file_path]
                subprocess.run(command, check=True)
                print(f'Successfully installed {file}')
            except subprocess.CalledProcessError as e:
                print(f'Failed to install {file}: {e}')

        # 创建标志文件，标记脚本已成功执行
        with open(flag_file, 'w') as f:
            f.write("Installation done.")
        print("Installation completed, flag file created.")
        display.stop()
        os.execv(sys.executable, ['python3'] + sys.argv)
    else:
        print("Login failed")
finally:
    if driver.current_url != target_url:
        driver.quit()
    
