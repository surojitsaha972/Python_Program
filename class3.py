class ABC:
    class_var=0
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var
        print("Object variable:-",var)
        print("Class object:-",ABC.class_var)
obj1=ABC(10)
obj2=ABC(20)