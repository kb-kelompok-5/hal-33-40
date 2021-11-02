# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionToefl500(Action):

    def name(self) -> Text:
        return "action_toefl500"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        test_message = "empty"
        message = "empty"
        for e in entities:
            if e['entity'] == 'prodi':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 5")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 500")

        return []

class ActionToefl400(Action):

    def name(self) -> Text:
        return "action_toefl400"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodi400':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 3")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 400")

        return []

class ActionToefl425(Action):

    def name(self) -> Text:
        return "action_toefl425"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodi425':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 3,5")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 425")

        return []

class ActionToefl450(Action):

    def name(self) -> Text:
        return "action_toefl450"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        test_message = "empty"
        message = "empty"
        for e in entities:
            if e['entity'] == 'prodi450':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 4")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 450")

        return []

class ActionToeflDiploma(Action):

    def name(self) -> Text:
        return "action_toefldiploma"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodidiploma':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 3")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 400")

        return []

class ActionToeflMagister450(Action):

    def name(self) -> Text:
        return "action_toeflmagister450"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodimagister450':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 4")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 450")

        return []

class ActionToeflMagister500(Action):

    def name(self) -> Text:
        return "action_toeflmagister500"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodimagister500':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 5")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 500")

        return []

class ActionToeflMagister525(Action):

    def name(self) -> Text:
        return "action_toeflmagister525"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodimagister525':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 5,5")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 525")

        return []

class ActionToeflDoktor450(Action):

    def name(self) -> Text:
        return "action_toefldoktor450"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodidoktor450':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 4")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 450")

        return []

class ActionToeflDoktor500(Action):

    def name(self) -> Text:
        return "action_toefldoktor500"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodidoktor500':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 5")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 500")

        return []

class ActionToeflDoktor475(Action):

    def name(self) -> Text:
        return "action_toefldoktor475"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities = tracker.latest_message['entities']
        message = "empty"
        test_message = "empty"
        for e in entities:
            if e['entity'] == 'prodidoktor475':
                message = e['value']
                message = message.title()

            if e['entity'] == 'test':
                test_message = e['value']

        if message == "empty":
            dispatcher.utter_message(text="Maaf prodi yang anda masukkan tidak ditemukan, silahkan masukkan nama lengkap prodi anda")
        else:
            if test_message == "IELTS":
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 4,5")
            else:
                dispatcher.utter_message(text=f"Skor {test_message} minimal untuk prodi {message} adalah 475")

        return []
