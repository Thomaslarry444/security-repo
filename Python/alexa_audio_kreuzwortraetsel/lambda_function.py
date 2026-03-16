"""Alexa Skill Lambda Entry Point für ein Audio-Kreuzworträtsel."""

from __future__ import annotations

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_intent_name, is_request_type
from ask_sdk_model import Response

from engine import CrosswordGame


GAME_KEY = "game"
CURRENT_CLUE_KEY = "current_clue"


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        session = handler_input.attributes_manager.session_attributes
        session[GAME_KEY] = CrosswordGame.with_sample_puzzle()
        clue = session[GAME_KEY].next_open_clue()
        session[CURRENT_CLUE_KEY] = clue.clue_id if clue else None

        speech = (
            "Willkommen beim Audio Kreuzworträtsel. "
            "Du kannst antworten mit: Die Lösung ist ... "
            f"Starten wir. {session[GAME_KEY].format_clue(clue)}"
        )
        return (
            handler_input.response_builder
            .speak(f"<speak><prosody rate='slow'>{speech}</prosody></speak>")
            .ask("Bitte nenne deine Lösung.")
            .response
        )


class AnswerIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AnswerIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        session = handler_input.attributes_manager.session_attributes
        game: CrosswordGame = session[GAME_KEY]
        clue_id = session[CURRENT_CLUE_KEY]
        answer = handler_input.request_envelope.request.intent.slots["answer"].value or ""

        if game.check_answer(clue_id, answer):
            if game.is_finished():
                speech = "Super, alle Hinweise sind gelöst. Möchtest du ein neues Rätsel starten?"
                reprompt = "Sage: neues Rätsel."
            else:
                next_clue = game.next_open_clue()
                session[CURRENT_CLUE_KEY] = next_clue.clue_id
                speech = f"Richtig. Nächster Hinweis: {game.format_clue(next_clue)}"
                reprompt = "Bitte nenne deine Lösung."
        else:
            speech = "Das war leider nicht korrekt. Sage Hinweis für einen Tipp oder versuche es erneut."
            reprompt = "Du kannst sagen: Hinweis."

        return handler_input.response_builder.speak(speech).ask(reprompt).response


class HintIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("HintIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        session = handler_input.attributes_manager.session_attributes
        game: CrosswordGame = session[GAME_KEY]
        clue_id = session[CURRENT_CLUE_KEY]
        hint = game.hint_for(clue_id)
        speech = f"Hier ist dein Tipp. {hint}"
        return handler_input.response_builder.speak(speech).ask("Wie lautet deine Lösung?").response


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speech = "Sage zum Beispiel: Die Lösung ist Alexa. Oder sage Hinweis."
        return handler_input.response_builder.speak(speech).ask(speech).response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_intent_name("AMAZON.CancelIntent")(handler_input) or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return handler_input.response_builder.speak("Bis bald und viel Erfolg beim nächsten Rätsel.").response


class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input: HandlerInput) -> bool:
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return handler_input.response_builder.response


sb = SkillBuilder()
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AnswerIntentHandler())
sb.add_request_handler(HintIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

lambda_handler = sb.lambda_handler()
