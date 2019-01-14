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
check_click("1545370878741.png", 2)

    
sign = "sign.png"

if exists(sign):
    print("find sign")
    check_click(Pattern("1536814622496.png").similar(0.85), 2)
    click_sleep(sign, 5)
    check_click("1541135091392.png", 1)
    check_click("1542449267862.png", 10)
      

    check_click(Pattern("1536294368703.png").similar(0.83), 2)
     
    check_click(Pattern("1533615527529.png").similar(0.94), 1)
        
    #sleep(5)

    #click("1533706172680.png")


    sleep(2)


wheel("1540790610381.png", WHEEL_DOWN, 8)

sleep(15)

unfinish = Pattern("1533615372888.png").similar(0.98)
bonus = Pattern("bonus.png").similar(0.86)
for i in findAll(unfinish):
    
    click_sleep(i, 2)

    check_click(Pattern("1541477041150.png").similar(0.84), 10)

    check_click(Pattern("1541477156477.png").similar(0.82), 10)
    
    click("1533613906973.png")
    sleep(3)
   
if exists(bonus):
    for i in findAll(bonus):
        print("find bonus")
        click_sleep(i, 5)
        click_sleep(Pattern("1533615527529.png").similar(0.94), 2)

click_sleep(Pattern("1545711231694.png").similar(0.83), 1)

click_sleep(Pattern("1536727093763.png").similar(0.81), 15)

click_sleep(Pattern("1536727151029.png").similar(0.89), 5)



click_sleep("1536727189343.png", 5)

click_sleep(Pattern("1545621409523.png").similar(0.81), 2)

click_sleep("1533615650190.png", 10)
click_sleep("1541136703643.png", 3)
click_sleep(Pattern("1533615718156.png").similar(0.72), 25)
wait_click("1535097385646.png", 5)

click_sleep("1535097417157.png", 5)
click_sleep("1535097438222.png", 10)
click_sleep("1533613906973.png", 10)


if exists(bonus):
    for i in findAll(bonus):
        print("find bonus")
        click_sleep(i, 2)
        click_sleep(Pattern("1533615527529.png").similar(0.94), 2)


















