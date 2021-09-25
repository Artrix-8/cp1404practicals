from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKm(App):
    """The class variable in the app is the 'model'."""
    # message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        # self.message = "Type in the field & press Enter"
        return self.root


ConvertMilesKm().run()
