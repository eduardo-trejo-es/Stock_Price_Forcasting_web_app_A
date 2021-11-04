
class PriceForcaster:
    def __init__(self):
        self.Selected_Company="null"

        

    def Gettingforcasting(self,Company):
        if Company=="TWTR":
            self.Selected_Company="Forscat of TWTR"
        elif Company=="AAPL":
            self.Selected_Company="Forscat of AAPL"
        else:
            self.Selected_Company=Company

        return self.Selected_Company