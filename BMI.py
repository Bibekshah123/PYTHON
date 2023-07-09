class BMI:
    def __init__(self):
        self.height=0.0
        self.weight=0.0
    def set_weight(self,weight):
        self.weight=weight
    def set_height(self,height):
        self.height=height
    def __call_BMI(self):
        BMI=self.weight/((self.height)**2)
        return BMI
    def display_BMI(self):
        BMI=self.__call_BMI()
        print(f"Your BMI is {round(BMI,2)}")
def main():
    bibek=BMI()
    user_weight=float(input("Enter your weight:"))
    user_height=float(input("Enter your height:"))
    bibek.set_weight(user_weight)
    bibek.set_height(user_height)
    bibek.display_BMI()
if(__name__)=="__main__":
    main()