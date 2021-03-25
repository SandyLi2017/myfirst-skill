from mycroft import MycroftSkill, intent_file_handler


class Myfirst(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('myfirst.intent')
    def handle_myfirst(self, message):
        self.speak_dialog('myfirst')


def create_skill():
    return Myfirst()

