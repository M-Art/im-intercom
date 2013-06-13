import kivy
import urllib
kivy.require('1.7.1')

from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty, BooleanProperty, StringProperty, ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.core.audio import SoundLoader


class LoginScreen(GridLayout):

     def zaloguj_callback(self, instance):
         if self.adres.text and self.nazwa.text:
             a = 'http://' + self.adres.text + '/login'
       params = urllib.urlencode({'@name': self.nazwa.text, '@adres': self.adres.text})
	     req = UrlRequest(a,  req_body=params)

     def wyloguj_callback(self, instance):
         a = 'http://' + self.adres.text + '/logout'
         params = urllib.urlencode({'@name': self.nazwa.text, '@adres': self.adres.text})
	 req = UrlRequest(a, req_body=params)


     def __init__(self, **kwargs):
         super(LoginScreen, self).__init__(**kwargs)
         self.cols = 2

         self.add_widget(Label(text='Nazwa'))

         self.nazwa = TextInput(multiline=False, font_size=40)
         self.add_widget(self.nazwa)

         self.add_widget(Label(text='Adres'))

         self.adres = TextInput(multiline=False, font_size=40)
         self.add_widget(self.adres)

	 self.add_widget(Label(text='Adres domofonu'))

	 self.adres_domofonu = TextInput(multiline=False, font_size=40)
	 self.add_widget(self.adres_domofonu)

	 self.zaloguj_button = Button(text='Zaloguj')
         self.zaloguj_button.bind(on_press=self.zaloguj_callback)
	 self.add_widget(self.zaloguj_button)

	 self.wyloguj_button = Button(text='Wyloguj')
         self.wyloguj_button.bind(on_press=self.wyloguj_callback)
	 self.add_widget(self.wyloguj_button)



class MyApp(App):

     def build(self):
         return LoginScreen()


if __name__ == '__main__':
     MyApp().run()
