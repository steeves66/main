from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    
    # def ready(self):
    #     @receiver(send_confirm_register_email)
    #     def send_confirm_register_email(sender, **kwargs):
    #         send_confirm_register_email(sender, **kwargs)
            
            
            
    def ready(self):
        import users.signals
    

