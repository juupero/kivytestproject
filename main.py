from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_string("""
<Boxes>:
    boxes: _boxes
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'top'
        ScreenManager:
            size_hint: 1, .9
            id: _screen_manager
            Screen:
                name: 'screen1'
                BoxLayout:
                    orientation: 'vertical'
                    padding: 50
                    id: _boxes
            Screen:
                name: 'screen2'
                Label:
                    text: 'Another Screen'
    AnchorLayout:
        anchor_x: 'left'
        anchor_y: 'top'
        BoxLayout:
            orientation: 'vertical'
            size_hint: .2, .1
            Button:
                text: 'Go to Screen 1'
                on_press: _screen_manager.current = 'screen1'
            Button:
                text: 'Go to Screen 2'
                on_press: _screen_manager.current = 'screen2'""")

class Boxes(FloatLayout):
    def __init__(self, **kwargs):
        super(Boxes, self).__init__(**kwargs)
        bx1 = BoxLayout(orientation='horizontal')
        bx2 = BoxLayout(orientation='horizontal')
        bx3 = BoxLayout(orientation='horizontal')
        bx4 = BoxLayout(orientation='horizontal')

        for i in range(1,2):
            bx1.add_widget(Button(text=str(i)))
        for i in range(2,5):
            bx2.add_widget(Button(text=str(i)))
        for i in range(5,7):
            bx3.add_widget(Button(text=str(i)))
        for i in range(7,11):
            bx4.add_widget(Button(text=str(i)))

        self.boxes.add_widget(bx1)
        self.boxes.add_widget(bx2)
        self.boxes.add_widget(bx3)
        self.boxes.add_widget(bx4)


class TestApp(App):
    def build(self):
        return Boxes()

if __name__ == '__main__':
    TestApp().run()