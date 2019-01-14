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
    
click_sleep("1545622261810.png", 20)
check_click("1545713065225.png", 10)
check_click("1545621928708.png", 15)

check_click("1545621959376.png",10)

check_click("1545622010542.png", 2)


click_sleep("1542449721942.png", 5)

click_sleep("1542449745802.png", 30)


click_sleep("1542449780851.png", 10)

click_sleep("1542449818389.png", 3)

click_sleep("1542449841645.png", 10)


click_sleep(Pattern("1542449884468.png").similar(0.89), 20)


check_click("1542603272752.png", 2)

    

click_sleep("1542449940273.png", 10)

click_sleep("1542450029900.png", 5)
click_sleep("1542450029900.png", 5)
click_sleep("1542450029900.png", 10)


check_click("1542449841645.png", 10)
click(Pattern("1542450042988.png").similar(0.83))

click("1542450080763.png")


lable="1543404518074-1.png"
count = 4
while exists(lable) and count:
    click_sleep(lable, 10)
    check_click("1545713329760-1.png", 2)
    check_click("1543404675939-1.png", 2)
    check_click("1544071139854-1.png", 5)    

    check_click("1544071102095-1.png", 5)
    check_click(Pattern("1544071456316-1.png").similar(0.87), 2)
    check_click("1544071496611-1.png", 2)

    click_sleep("1544071696172-1.png", 5)

    re_enter()
    count = count - 1


        

