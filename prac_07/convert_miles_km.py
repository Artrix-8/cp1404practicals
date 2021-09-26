from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    output_km = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * MILES_TO_KM)

    def handle_increment(self, text, increment):
        miles = self.convert_to_number(text) + increment
        self.root.ids.user_input.text = str(miles)
        self.update_result(miles)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKm().run()
