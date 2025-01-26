from appium import webdriver
from selenium.webdriver.common.by import By
import time

# 配置 Appium 连接
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.0",  # 请根据实际设备的 Android 版本修改
    "deviceName": "YourDeviceName",  # 请替换为实际设备名称
    "appPackage": "com.netease.cloudmusic",  # 网易云音乐的包名
    "appActivity": "com.netease.cloudmusic.activity.WelcomeActivity",  # 启动活动
    "noReset": True  # 不重置应用数据
}

# 初始化驱动
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # 等待应用加载
    time.sleep(5)

    # 前往消息和隐私设置页面
    driver.find_element(By.ACCESSIBILITY_ID, "消息和隐私设置").click()  # 假设按钮是通过可访问性ID定位的
    time.sleep(2)

    # 点击消息通知设置
    driver.find_element(By.ACCESSIBILITY_ID, "消息通知设置").click()
    time.sleep(2)

    # 修改通知选项（假设有铃声和震动选项可供修改）
    # 选择铃声选项
    driver.find_element(By.ACCESSIBILITY_ID, "铃声").click()
    time.sleep(1)
    # 选择一个自定义铃声（假设列表中有一个可选铃声）
    driver.find_element(By.XPATH, "//android.widget.TextView[@text='自定义铃声']").click()
    time.sleep(1)

    # 开启震动
    driver.find_element(By.ACCESSIBILITY_ID, "震动").click()
    time.sleep(1)

    # 点击保存按钮
    driver.find_element(By.ACCESSIBILITY_ID, "保存").click()
    time.sleep(2)

    # 验证设置是否保存
    # 这里可以通过查找特定的元素或者文本来验证设置是否生效
    # 假设有一个元素显示当前的通知设置
    current_setting = driver.find_element(By.ID, "current_notification_setting").text  # 请根据实际ID修改
    assert "自定义铃声" in current_setting, "铃声设置未保存"
    assert "震动开启" in current_setting, "震动设置未保存"

    print("测试通过：通知设置已成功保存")

except Exception as e:
    print(f"测试失败: {e}")

finally:
    # 关闭驱动
    driver.quit()
