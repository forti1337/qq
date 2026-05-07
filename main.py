from kivy.app import App
from kivy.uix.button import Button

class XHApp(App):
    def build(self):
        # Создаем кнопку с зеленым фоном
        return Button(
            text='XH System: Online', 
            background_color=(0.1, 0.8, 0.1, 1),
            font_size='25sp'
        )

if __name__ == '__main__':
    XHApp().run()
    
