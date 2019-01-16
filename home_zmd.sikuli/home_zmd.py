import helper
    
check_click("1547643205779.png", 5)

check_click(Pattern("1547645290107.png").similar(0.86), 2)
check_click("1547645104328.png", 2)

    
sign = "sign.png"

if exists(sign):
    print("find sign")
    check_click(Pattern("1536814622496.png").similar(0.85), 2)
    click_sleep(sign, 3)
    check_click("1541135091392.png", 1)
    check_click("1542449267862.png", 3)
      

    check_click(Pattern("1536294368703.png").similar(0.83), 2)
     
    check_click(Pattern("1533615527529.png").similar(0.94), 1)
        
    #sleep(5)

    #click("1533706172680.png")


    sleep(2)


wheel("1547645882709.png", WHEEL_DOWN, 8)

sleep(3)

unfinish = Pattern("unfinish.png").similar(0.85)
bonus = Pattern("bonus.png").similar(0.83)
fin = Pattern("1547646582587.png").similar(0.63)
for i in findAll(unfinish):
    
    click_sleep(i, 1)

    check_click(fin, 2)

    check_click(Pattern("1547646007378.png").similar(0.81), 2)
    
    click("1547646147750.png")
    sleep(1)
   
if exists(bonus):
    for i in findAll(bonus):
        print("find bonus")
        click_sleep(i, 1)
        click_sleep("1547647328230.png", 2)

click_sleep(Pattern("1545711231694.png").similar(0.68), 1)

click_sleep(fin, 2)

click_sleep("1547647454109.png", 3)


click_sleep("1547646147750.png", 2)

click_sleep(Pattern("1545621409523-4.png").similar(0.66), 2)

click_sleep(fin, 2)
click_sleep("1547647527476.png", 3)
click_sleep("1547647541173.png", 10)
wait_click("1547647592595.png", 5)

click_sleep("1535097417157-4.png", 5)
click_sleep("1535097438222-4.png", 10)
click_sleep("1547646147750.png", 10)


if exists(bonus):
    for i in findAll(bonus):
        print("find bonus")
        click_sleep(i, 2)
        click_sleep(Pattern("1533615527529-4.png").similar(0.94), 2)
    
