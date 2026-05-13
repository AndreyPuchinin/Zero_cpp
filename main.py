from notification_classes import error
err1 = error.error()
err1.create_notification('error bad')
err1.create_notification('error good')
err1.get_all_notifications()



print("Zero first version!")