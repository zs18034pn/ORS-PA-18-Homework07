"""
===================   TASK 5  ====================
* Create class Vehicle which represents any 
* vehicle and carries general info about the 
* vehicle like: company that built that vehicle, 
* model of the vehicle, year of production, 
* registration number, engine power and color.
* Create method cost_of_registration() that will 
* return how much will registration cost for that 
* instance of vehicle.
*
* Use this formula:

     - Production year fees: 100 EUR  if production year < 1990
                             200 EUR  if production year < 2000
                             300 EUR  if production year < 2010 
                             400 EUR  if production year < 2020
     - On production year fee add engine fee:   (engine power in kw * 2 EUR)
*
* In your main function create single instance of the
* Vehicle class and demonstrate the use of
* cost_of_registration method.
===================================================
"""

# Write your class here


class Vehicle:
    def __init__(self, company, model, year, regNum, enginepow, color):
        self.company = company
        self.model = model
        self.year = int(year)
        self.regNum = regNum
        self.enginePow = float(enginepow)
        self.color = color

    def cost_of_registration(self):

        if self.year < 1990:
            year_fees = 100
        elif self.year < 2000:
            year_fees = 200
        elif self.year < 2010:
            year_fees = 300
        else:
            year_fees = 400

        registration_cost = year_fees + (int(self.enginePow) * 2)
        print("The registration for this car would cost {0} EUR".format(registration_cost))




def main():
    # Test your function here
    info = Vehicle("Kia", "Ceed", 2005, "AM536", 149, "grey")
    info.cost_of_registration()

    pass


if __name__ == "__main__":
    main()
