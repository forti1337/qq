from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class XHThemeApp(App):
    def build(self):
        self.root = FloatLayout()
        
        # Фон-картинка (miku_bg.jpg должна быть в репозитории)
        self.bg_image = Image(source='miku_bg.jpg', allow_stretch=True, keep_ratio=False, opacity=0)
        self.root.add_widget(self.bg_image)

        # Однотонный фон для тем Dark/Light
        with self.root.canvas.before:
            self.bg_color = Color(0.1, 0.1, 0.1, 1)
            self.bg_rect = Rectangle(size=Window.size, pos=(0,0))
        
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.label = Label(text='XH MIKU EDITION', font_size='30sp', bold=True, color=(0, 1, 1, 1))
        layout.add_widget(self.label)

        self.theme_spinner = Spinner(
            text='Dark',
            values=('Dark', 'Light', 'Miku'),
            size_hint=(1, 0.2),
            background_color=(0.2, 0.2, 0.2, 1)
        )
        self.theme_spinner.bind(text=self.change_theme)
        layout.add_widget(self.theme_spinner)

        btn_exit = Button(text='ВЫХОД', size_hint=(1, 0.2), background_color=(0.8, 0, 0, 1))
        btn_exit.bind(on_press=self.stop)
        layout.add_widget(btn_exit)

        self.root.add_widget(layout)
        return self.root

    def change_theme(self, spinner, text):
        if text == 'Miku':
            self.bg_image.opacity = 1
            self.label.text = "MIKU MODE ACTIVE"
            self.label.color = (0, 1, 1, 1)
        elif text == 'Light':
            self.bg_image.opacity = 0
            self.bg_color.rgba = (0.9, 0.9, 0.9, 1)
            self.label.color = (0, 0, 0, 1)
        else:
            self.bg_image.opacity = 0
            self.bg_color.rgba = (0.1, 0.1, 0.1, 1)
            self.label.color = (0, 1, 0, 1)

if __name__ == '__main__':
    XHThemeApp().run()
        
