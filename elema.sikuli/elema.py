click("1536298774829.png")

sleep(5)

click("1536298819141.png")

sleep(3)

click("1536298862210.png")

sleep(5)

count = 400

butt = "1536299482112.png"

wheel(butt, WHEEL_DOWN, 3)

bonus = Pattern("bonus.png").targetOffset(152,0)

while count:
    if exists(bonus):
        click(bonus)

    count = count - 1

