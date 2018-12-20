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
    
check_click("1540790334473.png", 5)

check_click(Pattern("1536814622496.png").similar(0.85), 2)
check_click(Pattern("1533613772075.png").similar(0.83), 2)

    
sign = "sign.png"

if exists(sign):
    print("find sign")
    click_sleep(sign, 5)
    check_click("1541135091392.png", 1)
    check_click("1542449267862.png", 10)
      

    check_click(Pattern("1536294368703.png").similar(0.94), 2)
     
    check_click(Pattern("1533615527529.png").similar(0.94), 1)
        
    #sleep(5)

    #click("1533706172680.png")


    sleep(2)


wheel("1540790610381.png", WHEEL_DOWN, 8)

sleep(15)

unfinish = Pattern("1533615372888.png").similar(0.93)
bonus = Pattern("bonus.png").similar(0.86)
for i in findAll(unfinish):
    
    click_sleep(i, 2)

    check_click(Pattern("1541477041150.png").similar(0.84), 1)

    check_click(Pattern("1541477156477.png").similar(0.82), 2)
    

    if exists("1544072549930.png"):
        click("1533613906973.png")
    if exists("1535948744547.png"):
        click("1533613906973.png")
    if exists(Pattern("1543403911200.png").similar(0.83)):
        click("1543403924500.png")
    check_click(Pattern("1537159170533.png").similar(0.75), 2)


if exists(bonus):
    for i in findAll(bonus):
        print("find bonus")
        click_sleep(i, 2)
        click_sleep(Pattern("1533615527529.png").similar(0.94), 2)

click_sleep("1544072801586.png", 1)

click_sleep(Pattern("1536727093763.png").similar(0.81), 5)

wait_click("1536727151029.png", 5)


click_sleep("1536727189343.png", 5)

click_sleep("1544072859975.png", 2)

click_sleep("1533615650190.png", 10)
click_sleep("1541136703643.png", 3)
click_sleep(Pattern("1533615718156.png").similar(0.72), 20)
wait_click("1535097385646.png", 5)

click_sleep("1535097417157.png", 5)
click_sleep("1535097438222.png", 10)
click_sleep("1533613906973.png", 10)

click(bonus) 

click_sleep(Pattern("1533615527529.png").similar(0.96), 10)

click_sleep("1536727189343.png", 2)
click(bonus) 

click(Pattern("1533615527529.png").similar(0.96))

click(bonus)

click(Pattern("1533615527529.png").similar(0.96))















