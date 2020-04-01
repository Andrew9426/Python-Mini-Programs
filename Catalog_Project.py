# This is an home appliances catalog that contains 7 classes.
#The classes are:
#1.catalog - the parent class
#2.large_appliances - child class that inherits catalog class
#3.small_apliances- child class that inherits catalog class
#4.refrigerator - child class for large_appliances
#5.gas_cooker- child class for large_appliances
#6.mixer- child class for small_appliances
#7.iron- child class for small_appliances

class catalog(object):
    """ This is the parent class.Generates 4 attributes(price,consumption,manufacturer,product_code"""

    objects_list = [] #the list of objects,that will be populated when an instance will be created
    clas = None # class variable will be used to find objects in a particular class in the list of objects.
    subclass = None # class variable will be used to find objects in a particular class in the list of objects.


    def __init__(self, price, consum, manufacturer, product_code):

        self.price = price
        self.consum = consum
        self.manufacturer = manufacturer
        self.product_code = product_code

        catalog.objects_list.append(self) # append the objects created to the objects_list


    def show_price(self):
        """Display the price"""
        print('The price is :', self.price,"Lei")

    def show_consumption(self):
        """Display the consumption"""
        print('The consumption is :', self.consum, "Kw")

    def show_manufacturer(self):
        """Display the manufactuer"""
        print('This product is produced by :',self.manufacturer)

    def sort_price(self):
        """Sort by price the objects from the onjects list"""
        for obj in sorted(catalog.objects_list, key = lambda obiect:obiect.price):
            print("-------------------")
            print(obj.subclass, obj.manufacturer, ":", obj.price ,"Lei")

    def sort_consum(self):
        """Sort by consmuption the objects from the onjects list"""
        for obj in sorted(catalog.objects_list, key = lambda obiect:obiect.manufacturer):
            print("-------------------")
            print(obj.subclass, obj.manufacturer, ":", obj.consum, "Kw/luna")

    def ob_manufacturer(self):
        """ Displays the objects from a manufacturer"""
        for obj in catalog.objects_list:
            if obj.manufacturer == self.manufacturer:
                print(obj.manufacturer, ":", obj.subclass)

    def find_subclass(self):
        """ Displays the objects from an certain subclass"""
        for obj in catalog.objects_list:
            if obj.subclass == self.subclass:
                print(obj.subclass, obj.manufacturer)







class large_appliances(catalog):
    """ This is the first child class that  inherits the class catalog """
    def __init__(self, price, consum, manufacturer, product_code, depth,width, height):

        super().__init__(price, consum, manufacturer, product_code)
        self.depth = depth
        self.width = width
        self.height = height

    def display_depth(self):
        """ Returns the product depth"""
        print('The product depth is :', self.depth)

    def display_width(self):
        """ Returns the product width"""
        print('The product width is :', self.width)

    def display_h(self):
        """ Displays the product height"""
        print('The product height is :', self.height)




class small_appliances(catalog):
    """ This is the second child class that  inherits the class catalog """
    def __init__ (self, price, consum, manufacturer, product_code, wire_lenght, battery):

        super().__init__(price, consum, manufacturer, product_code)
        self.wire_lenght = wire_lenght
        self.battery = battery

    def display_lenght(self):
        """ Displays the product lenght"""
        print('The lenght of the wire is :', self.wire_lenght)

    def display_battery(self):
        """ Displays the product battery capacity"""
        print('The battery has :', self.battery, "A")

class refrigerator(large_appliances, catalog):
    """" This is the child class for large_appliances and the grandchild class for Catalog. In this class the products from the refrigerator category will be defined."""
    clas = "large appliances" # populates the class variable
    subclass = "refrigerator" # populates the class variable
    def __init__(self, price, consum, manufacturer, product_code, depth,width, height, freezer_capacity, refrigerator_capacity):
        super().__init__(price, consum, manufacturer, product_code, depth, width, height)
        self.freezer_capacity = freezer_capacity
        self.refrigerator_capacity = refrigerator_capacity

    def refrigerator_characteristics(self):
        """ Returns all the refrigerator characteristics """
        print("**For the ",self.manufacturer, "refrigerator", ":" "**")
        print("-The price is :", self.price)
        print("-the consumption is :", self.consum)
        print("-the manufacturer is : ", self.manufacturer)
        print("-the product code is : ", self.product_code)
        print("-the depth is : ", self.depth)
        print("-the width is : ", self.width)
        print("-the height is : ", self.height)
        print("-the freezer capacity is :", self.freezer_capacity)
        print("-the refrigerator capacity is :", self.refrigerator_capacity)




class gas_cooker(large_appliances):
    """" This is the child class for large_appliances and the grandchild class for Catalog. In this class the products from the gas cooker category will be defined."""
    clas = "large appliances" # populates the class variable
    subclass = "gas cooker" # populates the class variable
    def __init__(self, price, consum, manufacturer, product_code, depth,width, height, burners_number):
        super().__init__(price, consum, manufacturer, product_code, depth,width, height)
        self.burners_number = burners_number

    def gas_cooker_characteristics(self):
        """ Returns all the gas cooker characteristics """

        print("**For the ", self.manufacturer, "gas cooker", ":" "**")
        print("-The price is :", self.price)
        print("-the consumption is :", self.consum)
        print("-the manufacturer is : ", self.manufacturer)
        print("-the product code is : ", self.product_code)
        print("-the depth is : ", self.depth)
        print("-the width is : ", self.width)
        print("-the height is : ", self.height)
        print("-the number of burners is :", self.burners_number)

class mixer(small_appliances):
    """" This is the child class for small_appliances and the grandchild class for Catalog. In this class the products from the mixer category will be defined."""
    clas = "small appliances" # populates the class variable
    subclass = "mixer" # populates the class variable
    def __init__(self, price, consum, manufacturer, product_code, wire_lenght, battery,rotation_pminute):
        super().__init__(price, consum, manufacturer, product_code, wire_lenght, battery)
        self.rotation_pminute = rotation_pminute

    def mixer_characteristics(self):
        """ Returns all the mixer characteristics """
        print("**For the ", self.manufacturer, "mixer", ":" "**")
        print("-The price is: ", self.pret)
        print("-the consumption is :", self.consum)
        print("-the manufacturer is : ", self.manufacturer)
        print("-the product code is : ", self.product_code)
        print("-the wire lenght is :",self.wire_lenght, "meters")
        print("-the battery capacity is : ",self.battery)
        print("-the number of rotations per minute is : ", self.rotation_pminute)


class iron(small_appliances):
    """" This is the child class for small_appliances and the grandchild class for Catalog. In this class the products from the iron category will be defined."""
    clas = "small appliances" # populates the class variable
    subclass = "iron" # populates the class variable
    def __init__(self, price, consum, manufacturer, product_code, wire_lenght, battery, tank_capacity):
        super().__init__(price, consum, manufacturer, product_code, wire_lenght, battery)
        self.tank_capacity = tank_capacity

    def iron_characteristics(self):
        """ Returns all the iron characteristics """
        print("**For the ", self.manufacturer, "iron", ":" "**")
        print("-The price is: ",self.price)
        print("-the consumption is :", self.consum)
        print("-the manufacturer is : ", self.manufacturer)
        print("-the product code is : ", self.product_code)
        print("-the wire lenght is :", self.wire_lenght, "meters")
        print("-the battery capacity is : ", self.battery)
        print("-the tank capacity is :", self.tank_capacity)

#Create object
obj1 = refrigerator(1000, 2.5, "Beko", 123456, 54, 60, 130,100,90)
obj2 = refrigerator(1200, 2.7, "Zanussi", 1384, 90, 70, 180, 90,89)
obj3 = gas_cooker(2000, 3.0, "Arctic", 99852, 55, 65, 132,4)
obj4 = gas_cooker(1200, 5.6, "Beko", 4335, 50, 60, 80, 4)
obj5 = mixer(300, 1.3, "Zanussi", 9872, 1.5, 14, 1000)
obj6 = mixer(340, 1.2, "Tefal",99876, 1.5, 12, 1000)
obj7 = iron(390, 3.4, "Samsung", 34225, 2.5, 18, 1)
obj8 = iron(550, 1.4, "Tefal", 23445, 2, 23, 0.9)


#obj1.sort_price()

#obj1.sort_consum()

#obj1.ob_manufacturer()

#obj2.find_subclass()









