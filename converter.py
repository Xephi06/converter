class Converter:
    """
    Class used to convert different units
    """

    def celsius_to_fahrenheit(self, temperature: float, direction: str) -> float:

        if direction == "c_to_f":
            return (temperature * 9/5) + 32
        elif direction == "f_to_c":
            return (temperature - 32) * 5/9
        else:
            return None

    def feet_to_meters(self, distance: float, direction: str) -> float:
        if direction == "f_to_m":
            return distance * 0.3048
        elif direction == "m_to_f":
            return distance / 0.3048
        else:
            return None

    def pounds_to_kilograms(self, weight: float, direction: str) -> float:

        if direction == "p_to_k":
            return weight * 0.453592
        elif direction == "k_to_p":
            return weight / 0.453592
        else:
            return None

    def run(self):

        keep_running = True
        while keep_running:
            print("Which conversion would you like to do ?\n")
            print("""
            (1) For Celsius to Fareinheit.
            (2) For farheineit to Celsius.
            (3) For feet to meters.
            (4) For meters to feet.
            (5) For pounds to kilos.
            (6) For kilos to pounds
            (7) Stop the application
            """)
            user_input = input()
            while str(user_input) not in ["1", "2", "3", "4", "5", "6", "7"]:
                user_input = input("Wrong input try again !")

            if user_input == "1":
                value_to_convert = float(input("Enter value in Celsius : "))
                converted_value = self.celsius_to_fahrenheit(value_to_convert, "c_to_f")
                print(f"Value in Celsius : {converted_value}")
            elif user_input == "2":
                value_to_convert =  float(input("Enter the value in Fahreineit : "))
                converted_value = self.celsius_to_fahrenheit(value_to_convert, "f_to_c")
                print(f"Value in Fahreinheit : {converted_value}")
            elif user_input == "3":
                value_to_convert =  float(input("Enter the value in feet : "))
                converted_value = self.feet_to_meters(value_to_convert, "f_to_m")
                print(f"Value in meters : {converted_value}")
            elif user_input == "4":
                value_to_convert =  float(input("Enter the value in meters : "))
                converted_value = self.feet_to_meters(value_to_convert, "m_to_f")
                print(f"Value in feet : {converted_value}")
            elif user_input == "5":
                value_to_convert =  float(input("Enter the value in pounds :"))
                converted_value = self.pounds_to_kilograms(value_to_convert, "p_to_k")
                print(f"Value in kilos : {converted_value}")
            elif user_input == "6":
                value_to_convert = value_to_convert =  float(input("Enter the value in kilos :"))
                converted_value = self.pounds_to_kilograms(value_to_convert, "k_to_p")
                print(f"Value in pounds : {converted_value}")
            elif user_input == "7":
                keep_running = False
