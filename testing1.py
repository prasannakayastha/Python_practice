class Car():
    def __init__(self,model,year):
        self.year=year
        self.model=model
        self.hire= False
        
    def hired(self):
        if self.hire==False:
            
            print("Car is  available")
        else:
           
            print("Car is not available")    
        
    def returned(self):
        if self.hire==False:
            self.hire=True
            print("Car is returned")
            
        else:
            
            print("Car is hire")
                
        
    def show_detail(self):
            if self.hire==False:
                print(f"{self.model} : Available") 
                
            else:
                
                print(f"{self.model} :  Not Available")   
                
car1 = Car("Toyota Corolla", "2018")
car2 = Car("Honda Civic", "2020")
car3 = Car("Ford Mustang", "1967")
car4 = Car("Chevrolet Camaro", "2019")
car5 = Car("Mazda MX-5 Miata", "1990")
car6 = Car("Volkswagen Golf", "2015")
car7 = Car("BMW 3 Series", "2021")
car8 = Car("Audi A4", "2017")
car9 = Car("Mercedes-Benz C300", "2016")
car10 = Car("Subaru Impreza", "2022")


car1.hired()
car1.show_detail()  
car1.returned()
car1.show_detail()

car1.hired()       
                