class SampleClass:
    name ={"p1":"an"
          , "p2":"adna"
          ,"p3":"afnskdf"}
    for count,key in enumerate(name):
        print(f"{count}:{key}")

    #default constructor which is initialize the val
    def __init__(self):
        #key are initalized with
        #thir respective val
        self.exmp1 ='2'
        self.exmp2 ="3"
        self.exmp3 ="3"
        self.exmp4 ="3"
     #printDict method which print some sample text
    def printDict(self):
        print("dict const from obj field of the class sampleclass")
#crearting an obj to represent the class
sampleobj = SampleClass()
sampleobj.name
for count,key in enumerate(sampleobj.name):
    print(f"{count}:{key}")
#calling printit method
#sampleobj.printDict()
#calling obj __dict__ on sampleclass obj and print it
print(sampleobj.__dict__)
