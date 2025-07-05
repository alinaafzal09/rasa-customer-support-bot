from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionProcessOrderIssue(Action):

    def name(self) -> Text:
        return "action_process_order_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Fetch the order ID from the slot
        order_id = tracker.get_slot("order_id")

        if order_id:
            # Send confirmation to user
            dispatcher.utter_message(text=f"Thank you. Your issue has been registered for Order ID: {order_id}. Our team will contact you soon.")
        else:
            dispatcher.utter_message(text="Please provide a valid Order ID.")

        return []

