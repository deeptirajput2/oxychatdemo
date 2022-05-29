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


class AskSugarLevel(Action):
    def name(self) -> Text:
        return "ask_sugar_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="did you check your sugar level?")

        return []


class AskSleepQuality(Action):
    def name(self) -> Text:
        return "ask_sleep_quality"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="did you sleep well?")

        return []


class AskSugarLevel(Action):
    def name(self) -> Text:
        return "ask_sugar_reading"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="what was your sugar reading?")

        return []


class AskChosenConcernLevel(Action):
    def name(self) -> Text:
        return "action_choose_concern"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_choice = tracker.get_slot("concern")
        if user_choice.lower() == "diabetes":
            dispatcher.utter_message(text="What is your fasting sugar number")
        else:
            dispatcher.utter_message(text=f"You chose {user_choice}, we are working on it")

        return []

class AskCheckSugar(Action):
    def name(self) -> Text:
        return "action_check_sugar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_choice = tracker.get_slot("fasting")
        if int(user_choice) < 130:
            dispatcher.utter_message(text="Please check and let us know your blood sugar 2 hours after breakfast")
        else:
            dispatcher.utter_message(text="Have you missed or reduced dose of your insulin at dinner time?")

        return []

class AskForgotMedicine(Action):
    def name(self) -> Text:
        return "action_forgot_medicine"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_choice = tracker.get_slot("missed_medicine")
        dispatcher.utter_message(text=f"did user forgot {user_choice}")

        # if user_choice == True:
        #     dispatcher.utter_message(text="Do not alter your medicines without speaking with your doctor. If you think that existing medicines are too strong, take a consultation from a Oxyjon Doctor.")
        # else:
        #     dispatcher.utter_message(text="Did you forgot to take your medicine last night")

        return []



