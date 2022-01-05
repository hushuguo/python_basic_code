has_ticket = True
knife_length = 30
if has_ticket:
    if knife_length > 20:
        print("不允许上车，你的刀长为%dcm" % knife_length)
    else:
        print("安检通过")
else:
    print("不允许进门")