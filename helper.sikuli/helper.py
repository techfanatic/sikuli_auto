def check_click(img_file, time):
    if not exists(img_file):
        print("%s not displayed" % img_file)
    if exists(img_file):
        click(img_file)
        sleep(time)
def wait_click(img_file, time):
    wait(img_file)
    click(img_file)
    sleep(time)

def click_sleep(img_file, time):
    click(img_file)
    sleep(time)
def re_enter():
    click_sleep("1545625043164.png", 5);
    click_sleep("1545625089314.png", 15)
