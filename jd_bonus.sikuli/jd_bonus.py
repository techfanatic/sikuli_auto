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
    
lable="1543404518074.png"
count = 3
while exists(lable) and count:
    click_sleep(lable, 10)
    check_click("1543404675939.png", 2)
    check_click("1544071139854.png", 5)    

    check_click("1544071102095.png", 5)
    check_click("1544071456316.png", 2)
    check_click("1544071496611.png", 2)

    click_sleep("1544071696172.png", 5)

    re_enter()
    count = count - 1

    
  
    

