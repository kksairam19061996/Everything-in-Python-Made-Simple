
def f1():
    print("f1 execution")
def f2():
    print("f2 execution")
def f3():
    print("f3 execution")    

if __name__=="__main__": # This will execute all the functions if it is called in the same module, if this module is imported, all the functions are available but will not execute.    
    f1()
    f2()
    f3()