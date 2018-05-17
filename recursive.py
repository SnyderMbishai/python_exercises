def hello_world(count):
    if count<1:
        print ("hello world")
        hello_world(count-1)


hello_world(10)
