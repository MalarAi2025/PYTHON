
class multipleFunctions():
    
    def Eligible():
        gender=input("Enter the gender")
        age=int(input("Enter the age"))
        if(gender=='female' and age<18):
            print("Not Eligible")
            msg='Not Eligible'
        elif(gender=='male' and age<21):
            print("Not Eligible")
            msg="Not Eligible"
        else:
            print("Eligible")
            msg="eligible"
            return msg
    def AreaOfTriangle():
          Height=int(input("Height="))
          Breadth=int(input("Breadth="))
          Area=((Height*Breadth)/2)
          print(Area)
          AreaOfTriangle=(input("Area of Triangle="),Area)
          return Area
    def Percentage():
         subject1=int(input("Subject1="))
         subject2=int(input("Subject2="))
         subject3=int(input("Subject3="))
         subject4=int(input("Subject4="))
         subject5=int(input("Subject5="))
         Total=(subject1+subject2+subject3+subject4+subject5)
         Percentage=((Total/500)*100)
         print("Percentage of total marks =",Percentage)
         return Percentage
    def OddEven(num):
        num=input("Enter the given number=")
        if(num%2==0):
           print(int(num),"is Even number")
        else:
          print(int(num),"is Odd number")
          return OddEven
    def Peri():
        Height1=int(input("Height1="))
        Height2=int(input("Height2="))
        Breadth1=int(input("Breadth1="))
        Perimeter=(Height1+Height2+Breadth1)
        print(Perimeter)
        Peri=(input("Perimeter of the Triangle="),Perimeter)
        return Peri
    def Subfields():
        List=["Machine learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for SubfieldsInAI in List:
           print(SubfieldsInAI)  
        return SubfieldsInAI
                
        
        
        
    
             
