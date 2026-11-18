"""
CP1404/CP5632 - Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder


class ConvertMilesKM(App):
    """SquareNumberApp is a Kivy App for squaring a number."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Handle calculation (could be button press or other call), output result to label."""
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = f"{result:.4f} km"
        except ValueError:
            self.root.ids.output_label.text = f"{0:.4f} km"
            # pass

    def handle_increment(self, value, other):
        """Increase or  decrease the input number by 1"""
        try:
            result = float(value) + other
            self.root.ids.input_number.text = str(result)
        except ValueError:
            result = 0 + other
            self.root.ids.input_number.text = str(result)

    def handle_clear(self):
        print("test")
        self.root.ids = ""


ConvertMilesKM().run()
