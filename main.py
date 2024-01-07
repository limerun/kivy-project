import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
class MyGrid(Widget):
    inp = ObjectProperty(None)
    lbl = ObjectProperty(None)
    spn = ObjectProperty(None)
    inpzing = ObjectProperty(None)
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    a = " "
    def btn(self):
        self.a = " "
        if self.spn.text == "sifruoti":
            for i in range(len(self.inp.text)):
                x = self.abc.index(self.inp.text[i])
                self.a += self.abc[x + int(self.inpzing.text)]
            self.lbl.text = self.a
        if self.spn.text == "desifruoti":
            for i in range(len(self.inp.text)):
                x = self.abc.index(self.inp.text[i])
                self.a += self.abc[x - int(self.inpzing.text)]
            self.lbl.text = self.a
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__ == "__main__":
    MyApp().run()