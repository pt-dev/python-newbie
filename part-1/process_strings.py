max_len = 79
str_plier = 2
foo = "Oh oh oh oh you don't know, Joe."*str_plier
curr_len = len(foo)

if curr_len > max_len:
    print("Danger, Will Robinson!!!")
    print("Your sentiment is {} ".format(curr_len-max_len)+"characters too long!")
else:
    print("What a lovely sentiment!\n"+ foo+"\nIn only {} characters!".format(curr_len))
