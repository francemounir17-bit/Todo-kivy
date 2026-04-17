from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

# إعداد لون خلفية بسيط (اختياري)
Window.clearcolor = (0.1, 0.1, 0.1, 1)

class TasbihApp(App):
    def build(self):
        self.count = 0  # العداد
        
        # تخطيط التطبيق بشكل عمودي
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # النص الذي يعرض الرقم
        self.label = Label(
            text="0", 
            font_size='100sp', 
            color=(0, 1, 0.7, 1) # لون تركواز
        )
        
        # زر الضغط (الزيادة)
        btn_count = Button(
            text="اضغط للتسبيح", 
            size_hint=(1, 0.4),
            background_color=(0, 0.7, 1, 1),
            font_size='25sp'
        )
        btn_count.bind(on_press=self.increment)
        
        # زر إعادة الضبط (الصفر)
        btn_reset = Button(
            text="إعادة ضبط", 
            size_hint=(1, 0.2),
            background_color=(1, 0.3, 0.3, 1),
            font_size='20sp'
        )
        btn_reset.bind(on_press=self.reset)
        
        # إضافة العناصر للشاشة
        layout.add_widget(self.label)
        layout.add_widget(btn_count)
        layout.add_widget(btn_reset)
        
        return layout

    def increment(self, instance):
        self.count += 1
        self.label.text = str(self.count)

    def reset(self, instance):
        self.count = 0
        self.label.text = "0"

if __name__ == '__main__':
    TasbihApp().run()
