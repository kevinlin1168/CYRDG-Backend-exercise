def f(num):
    try:
        return str(format(num, ','))
    except:
        print("An exception occurred")
        return None