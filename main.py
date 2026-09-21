from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    RoleManager = autoclass('android.app.role.RoleManager')
    Context = autoclass('android.content.Context')

class CallBlockerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(
            text="Unknown Call Blocker\n(Default Dialer)",
            font_size='20sp',
            halign='center'
        )
        
        self.btn = Button(
            text="Make Default Dialer",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)
        )
        self.btn.bind(on_press=self.request_default_dialer)
        
        layout.add_widget(self.label)
        layout.add_widget(self.btn)
        return layout

    def request_default_dialer(self, instance):
        if platform == 'android':
            try:
                activity = PythonActivity.mActivity
                role_manager = activity.getSystemService(Context.ROLE_SERVICE)
                
                if role_manager.isRoleAvailable(RoleManager.ROLE_DIALER):
                    if not role_manager.isRoleHeld(RoleManager.ROLE_DIALER):
                        intent = role_manager.createRequestRoleIntent(RoleManager.ROLE_DIALER)
                        activity.startActivityForResult(intent, 1)
                        self.label.text = "Status: Default Dialer Requested!"
                    else:
                        self.label.text = "Status: Already Default Dialer!"
            except Exception as e:
                self.label.text = f"Error: {str(e)}"
        else:
            self.label.text = "Run this on Android Device"

if __name__ == '__main__':
    CallBlockerApp().run()
