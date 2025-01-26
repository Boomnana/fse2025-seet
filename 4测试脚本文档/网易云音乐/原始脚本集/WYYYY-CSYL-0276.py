from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 配置 Appium 连接
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.0",  # 请根据实际设备的 Android 版本修改
    "deviceName": "YourDeviceName",  # 请替换为实际设备名称
    "appPackage": "com.netease.cloudmusic",  # 网易云音乐的包名
    "appActivity": "com.netease.cloudmusic.activity.WelcomeActivity",  # 启动活动
    "noReset": True,  # 不重置应用数据
    "automationName": "UiAutomator2"
}

# 初始化驱动
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# 定义显式等待
wait = WebDriverWait(driver, 20)

try:
    # 等待应用加载，并确认首页加载完成
    print("等待应用主页面加载...")
    wait.until(EC.presence_of_element_located((By.ID, "com.netease.cloudmusic:id/main_nav_settings")))

    # 前往桌面小部件设置（假设通过设置进入）
    print("进入设置页面...")
    driver.find_element(By.ID, "com.netease.cloudmusic:id/main_nav_settings").click()

    print("等待设置页面加载...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='桌面小部件']")))

    # 进入桌面小部件设置
    print("点击进入桌面小部件设置...")
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='桌面小部件']").click()

    # 等待桌面小部件设置页面加载
    print("等待桌面小部件设置页面加载...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='显示设置']")))

    # 点击“显示设置”选项
    print("点击显示设置...")
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='显示设置']").click()

    # 等待显示设置选项可用
    print("等待显示设置页面...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='颜色']")))

    # 设置小部件的外观 - 更改颜色（假设颜色选项可以通过ID选择）
    print("更改小部件颜色...")
    try:
        color_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='颜色']")))
        color_option.click()

        # 假设可以选择自定义颜色
        custom_color = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='自定义颜色']")))
        custom_color.click()

        print("颜色设置成功")
    except Exception as e:
        print(f"设置颜色时发生错误: {e}")

    # 设置小部件的尺寸（假设尺寸选项可以通过ID选择）
    print("更改小部件尺寸...")
    try:
        size_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='尺寸']")))
        size_option.click()

        # 选择一个自定义尺寸
        custom_size = wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='中']")))
        custom_size.click()

        print("尺寸设置成功")
    except Exception as e:
        print(f"设置尺寸时发生错误: {e}")

    # 保存设置并返回桌面查看效果
    print("保存设置并返回桌面...")
    driver.press_keycode(3)  # Android Home 按钮返回桌面
    time.sleep(5)  # 等待几秒以确保返回桌面

    # 验证小部件是否在桌面上正确显示（这里需要根据桌面上的小部件状态进行验证）
    print("验证桌面上的小部件...")
    try:
        # 假设小部件有一个可以识别的ID或可访问的属性
        widget_displayed = wait.until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='网易云音乐小部件']")))
        assert widget_displayed is not None, "小部件未在桌面上显示"
        print("小部件正确显示")
    except Exception as e:
        print(f"验证小部件时发生错误: {e}")

except Exception as e:
    print(f"测试失败: {e}")

finally:
    # 关闭驱动
    driver.quit()
