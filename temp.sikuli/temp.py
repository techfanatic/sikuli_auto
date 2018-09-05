aim = Pattern("aim.png").similar(0.92)

i = 10
while i:
    if Screen(0).exists(aim):
        click(Pattern("aim.png").similar(0.92).targetOffset(120,21))
        sleep(3)
        click("1536048196133.png")
   # if exists(aim2):
      #  click(aim2)

    i = i - 1



