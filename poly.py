class car:
    def _init_ (self,brand,model):
        self.brand=brand
        self.model=model

        def move(self):
            print("drive")


class truck:
    def _init_ (self,brand,model):
        self.brand=brand
        self.model=model

        def move(self):
            print("drive")

class boat:
    def _init_ (self,brand,model):
        self.brand=brand
        self.model=model

        def move(self):
            print("move")


car=car("ford","mustang")
truck=truck("volvo","fh16")
boat=boat("yamaha","212x")


for x in (car,truck,boat):
    x.move()