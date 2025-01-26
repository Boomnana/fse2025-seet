from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# appium-python-client 2.10.0
# selenium 4.10
# appium 1.17.1
# 网易云音乐 9.1.60
options = UiAutomator2Options().load_capabilities({
    "deviceName": "127.0.0.1:62001",
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.netease.cloudmusic",
    "appActivity": ".activity.IconChangeDefaultAlias",
    # 'noReset': True,
    # 在每次测试启动时，不重置应用的状态。
    # 这意味着应用在启动时会保留之前的用户数据和设置，例如登录信息和用户偏好。
    "unicodeKeyboard": True,
    # 输入非英文字符或特殊符号。
    "resetKeyboard": True,
    # 在测试结束后，恢复到原来的输入法或键盘设置
})

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
print('当前用例：在状态栏显示歌词')
size = driver.get_window_size()
# 获取屏幕宽度
width = size['width']

# 获取屏幕高度
height = size['height']

print(width)
print(height)
# app起始页（点同意）

try:
    sleep(8)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/agree")
    # 定位
    element.click()
    # 对元素进行操作

except Exception as e:
    print("起始页发生错误：", e)

sleep(1)

# app起始页（点允许）
try:
    sleep(1)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# app起始页（点击立即体验）
try:
    sleep(6)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/trialT")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# app起始页（点击同意）
try:
    sleep(1)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/positiveBtn")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# 进入首页（点击允许）
try:
    sleep(8)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button")
    # 定位
    element.click()
    # 对元素进行操作
except Exception as e:
    print("app起始页发生错误：", e)

# 首页-选项
try:
    sleep(8)
    # 等待元素加载完成
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/menu_icon")
    # 定位
    element.click()
    # 对元素进行操作

except Exception as e:
    print("首页-选项发生错误：", e)

# 首页-选项-滚动到设置并点击
try:
    sleep(5)
    # 等待元素加载完成
    # driver.tap([(340,739)])  # 原先元素的坐标

    x1 = int(width * 730 / 900)
    y1 = int(height * 1540 / 1600)
    x2 = int(width * 730 / 900)
    y2 = int(height * 416 / 1600)
    TouchAction(driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
    # 滚动到设置
    x3 = int(width * 676 / 900)
    y3 = int(height * 585 / 1600)
    TouchAction(driver).tap(x=x3, y=y3).perform()
    # 点击设置



except Exception as e:
    print("首页-选项-滚动到设置点击发生错误：", e)

# 首页-选项-设置-滚动
try:
    sleep(3)
    # 等待元素加载完成

    # 滚动到在状态栏显示歌词
    x1 = int(width * 406 / 900)
    y1 = int(height * 168 / 1600)
    x2 = int(width * 403 / 900)
    y2 = int(height * 1534 / 1600)
    TouchAction(driver).long_press(x=x1, y=y1).move_to(x=x2, y=y2).release().perform()
    sleep(1)  # 等待一秒钟以便观察效果
    #点击状态栏歌词设置
    x3 = int(width * 425 / 900)
    y3 = int(height * 1478 / 1600)
    TouchAction(driver).tap(x=x3, y=y3).perform()
    sleep(1)  # 等待一秒钟以便观察效果
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/useStatusLyricCb")
    # 定位dakai
    element.click()
    # 打开


except Exception as e:
    print("首页-选项-设置-滚动到状态栏歌词并打开：", e)

# 返回首页
try:
    sleep(1)
    # 等待元素加载完成
    # 模拟返回键
    driver.execute_script("mobile: pressButton", {"buttonName": "back"})
    driver.execute_script("mobile: pressButton", {"buttonName": "back"})
    sleep(1)
    # 等待元素加载完成

except Exception as e:
    print("返回首页：", e)

# 播放罗生门
try:
    sleep(1)
    # 等待元素加载完成
    x3 = int(width * 235 / 900)
    y3 = int(height * 109 / 1600)
    TouchAction(driver).tap(x=x3, y=y3).perform()
    # 点击搜索
    sleep(2)
    element = driver.find_element(By.ID, "com.netease.cloudmusic:id/search_src_text")
    # 定位
    element.send_keys('罗生门')
    # 对元素进行操作
    element1 = driver.find_element(By.ID, "com.netease.cloudmusic:id/toSearch")
    # 定位
    element1.click()
    # 点击搜索
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]"))
    )
    sleep(2)
    x3 = int(width * 231 / 900)
    y3 = int(height * 592 / 1600)
    TouchAction(driver).tap(x=x3, y=y3).perform()
    # 点击打开
except Exception as e:
    print("播放罗生门：", e)

# 回到桌面
try:
    sleep(3)
    driver.execute_script("mobile: pressButton", {"buttonName": "home"})

except Exception as e:
    print("回到桌面：", e)

# 回到桌面检查元素
try:
    sleep(3)
    # 等待并检查歌词元素是否存在（根据文本内容）
    wait = WebDriverWait(driver, 30)
    lyric_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[contains(@text, 'Wiz')]"))  # 替换为实际歌词文本
    )
    # 定位
    print("元素存在,测试通过")

except Exception as e:
    # 捕获异常，说明元素不存在
    print("元素不存在，测试不通过")

driver.quit()
