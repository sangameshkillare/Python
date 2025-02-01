class car:
    price=100
    gst=18/100
    total=price*gst
    
obj=car()
print(obj.price)

print(obj.gst)
print(f"total={obj.total}")