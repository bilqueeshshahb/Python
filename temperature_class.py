#3-5.create a temperature class.create 2 methods named convertFaranheit() &convertcelsius.()
class Temperature:
    @staticmethod
    def convertFaranheit(celsius):
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32
    
    @staticmethod
    def convertcelsius(fahrenheit):
        """Convert Fahrenheit to Celsius"""
        return (fahrenheit - 32) * 5/9

# Example usage
if __name__ == "__main__":
    # Convert 0°C to Fahrenheit
    print(f"0°C = {Temperature.convertFaranheit(0)}°F")
    
    # Convert 32°F to Celsius
    print(f"32°F = {Temperature.convertcelsius(32)}°C")
    
    # Convert 100°C to Fahrenheit
    print(f"100°C = {Temperature.convertFaranheit(100)}°F")
    
    # Convert 212°F to Celsius
    print(f"212°F = {Temperature.convertcelsius(212)}°C")
