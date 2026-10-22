def convert_temperature(value, from_unit, to_unit):
    valid_units = {"C", "F", "K"}
    if from_unit not in valid_units or to_unit not in valid_units:
        return None
    
    else:
        if from_unit == "C":
            celsius = value
        elif from_unit == "F":
            celsius = (value - 32) / 1.8
        elif from_unit == "K":
            celsius = value - 273.15

        if to_unit == "C":
            return celsius
        elif to_unit == "F":
            return (celsius * 1.8) + 32
        elif to_unit == "K":
            return celsius + 273.15

        
print(convert_temperature(20, "C", "X"))