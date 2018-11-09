click("1540792082363.png")

sleep(10)

click("1536298819141.png")

sleep(3)

if exists("1540791906070.png"):
    click("1540791920457.png")


sleep(3)
click("1541134556132.png")

sleep(8)

count = 400

butt = "butt.png"

if exists(butt):
    click(butt)
  
        
    sleep(5)
    if exists("1536728302365.png"):
        click("1536728312022.png")

        
    else: 
        if exists("1536727946502.png"):
            click("1536727946502.png")

            sleep(2)

            click("1537938034477.png")

            sleep(5)       
            click(Pattern("1536298862210.png").targetOffset(-38,-11))
        
sleep(1)

wheel("1536899668334.png", WHEEL_DOWN, 5)

bonus = Pattern("bonus.png").targetOffset(141,-7)

while count:
    if exists(bonus):
        click(bonus)

    count = count - 1

