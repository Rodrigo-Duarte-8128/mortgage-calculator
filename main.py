from kivy.app import App
from layout import Layout


class MyApp(App):
    def build(self):
        self.layout = Layout()
        return self.layout

if __name__ == "__main__":
    MyApp().run()