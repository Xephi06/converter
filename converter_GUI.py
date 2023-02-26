from tkinter import *
from converter import Converter

class ConverterGUI:
    def __init__(self, master):
        self.converter = Converter()

        # Create labels
        Label(master, text="Conversion type:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
        Label(master, text="Value:").grid(row=1, column=0, padx=5, pady=5, sticky=W)
        Label(master, text="Result:").grid(row=2, column=0, padx=5, pady=5, sticky=W)

        # Create option menu for conversion type
        self.conversion_type = StringVar(master)
        self.conversion_type.set("Celsius to Fahrenheit") # default value
        conversion_options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius", "Feet to Meters", "Meters to Feet", "Pounds to Kilograms", "Kilograms to Pounds"]
        OptionMenu(master, self.conversion_type, *conversion_options).grid(row=0, column=1, padx=5, pady=5)

        # Create entry box for value to convert
        self.value_entry = Entry(master)
        self.value_entry.grid(row=1, column=1, padx=5, pady=5)

        # Create label to display result
        self.result_label = Label(master, text="")
        self.result_label.grid(row=2, column=1, padx=5, pady=5)

        # Create button to initiate conversion
        Button(master, text="Convert", command=self.convert).grid(row=3, column=1, padx=5, pady=5)

    def convert(self):
        # Get user input
        conversion_type = self.conversion_type.get()
        value = float(self.value_entry.get())

        # Call appropriate conversion function from Converter class
        if conversion_type == "Celsius to Fahrenheit":
            result = self.converter.celsius_to_fahrenheit(value, "c_to_f")
        elif conversion_type == "Fahrenheit to Celsius":
            result = self.converter.celsius_to_fahrenheit(value, "f_to_c")
        elif conversion_type == "Feet to Meters":
            result = self.converter.feet_to_meters(value, "f_to_m")
        elif conversion_type == "Meters to Feet":
            result = self.converter.feet_to_meters(value, "m_to_f")
        elif conversion_type == "Pounds to Kilograms":
            result = self.converter.pounds_to_kilograms(value, "p_to_k")
        elif conversion_type == "Kilograms to Pounds":
            result = self.converter.pounds_to_kilograms(value, "k_to_p")

        # Update result label
        self.result_label.config(text=result)
