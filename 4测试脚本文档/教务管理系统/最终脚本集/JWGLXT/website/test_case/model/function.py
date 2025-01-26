import csv

# 后续再调整
# def get_screenshot(driver, filename):
#     file=f'D:/zhaojx/bigwork/ZCGLXT_PO/Website/test_report/srceenshot/{filename}'
#     driver.get_screenshot_as_file(file)

def get_data(file_path):
    data = []
    with open(file_path, 'r', encoding="utf-8") as file_object:
        f_csv = csv.reader(file_object)
        for row in f_csv:
            data.append(row)
    return data


