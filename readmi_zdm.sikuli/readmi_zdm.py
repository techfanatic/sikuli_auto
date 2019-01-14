import helper
    
check_click("1546841624109.png", 2)

check_click(Pattern("1536814622496.png").similar(0.85), 1)
check_click("1545788813448.png", 1)

    
sign = "sign.png"

if exists(sign):
    print("find sign")
    check_click(Pattern("1536814622496.png").similar(0.85), 1)
    click_sleep(sign, 1)
    #check_click("1545788965666.png", 1)
    check_click("1545789104538.png", 1)
      
   
    check_click(Pattern("1536294368703.png").similar(0.83), 1)
    wheel("1545789302757.png", WHEEL_DOWN, 5)
    sleep(3)

unfinish = Pattern("1545788965666.png").similar(0.93)
bonus = Pattern("bonus.png").similar(0.86)
back = "1545789323653.png"
todo = Pattern("1545789465658.png").similar(0.82)
confirm = Pattern("1545789573787.png").similar(0.89)
for i in findAll(unfinish):
    
    click_sleep(i, 1)

    check_click(todo, 2)

    check_click("1545789505800.png", 1)
    check_click(back, 1)
    check_click(Pattern("1545790275798.png").targetOffset(62,1), 2)
   
if exists(bonus):
    for i in findAll(bonus):
        print("find bonus")
        click_sleep(i, 2)
        click_sleep(confirm, 2)


click_sleep("1545791089459.png", 2)

click_sleep(todo, 3)
click_sleep("1546503662084.png", 3)
click_sleep("1546503675157.png", 5)
wait_click("1547016233492.png", 2)

click_sleep("1547016245564.png", 2)
click_sleep("1547016258848.png", 2)
click_sleep(back, 2)

click_sleep("1545789601623.png", 1)

click_sleep(todo, 2)

wait_click("1545789711672.png", 2)


click_sleep(back, 2)
if exists(bonus):
    for i in findAll(bonus):
        print("find bonus")
        click_sleep(i, 2)
        click_sleep(confirm, 2)