def func (action:str):
    def summ(x,y):
        return x+y
    def mlt(x,y):
        return x*y
    if(action=="summ"):
        return summ
    if (action == "mlt"):
        return mlt

if __name__ == '__main__':
    action=func("summ")
    print(action(2,3))
    action2=func("mlt")
    print(action2(2,3))
