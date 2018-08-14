#test
click("1533613746548.png")
sleep(5)

click("1533613772075.png")
sleep(2)

#click("1533613833999.png")
sign = Pattern("1533613852474.png").exact()

if exists(sign):
    print("find sign")
    click(sign)
    sleep(2)
    click("1533706148466.png")
    
    sleep(1)

    click("1533706172680.png")

click(Pattern("1533706666690.png").exact())

sleep(3)

unfinish = Pattern("1533615372888.png").similar(0.82)

for i in findAll(unfinish):
    
    click(i)
    sleep(1)

    click("1533615450308.png")

    sleep(2)


    click("1533613906973.png")

    sleep(2)


bonus = Pattern("1533615499991.png").exact()
if exists(bonus):
    print("find bonus")
    click(bonus) 
    click("1533615527529.png")



click("1533615635276.png")

click("1533615650190.png")

click("1533876315912.png")

click("1533615718156.png")













