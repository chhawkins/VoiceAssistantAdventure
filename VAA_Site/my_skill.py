from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type
from ask_sdk_core.utils import get_slot_value
from ask_sdk_model.ui import SimpleCard
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from VAA_Site.parsing.parseData import parse_data
from VAA_Site.game.game_state_machine import perform_action


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""

    def can_handle(self, handler_input):
        # if the request is LaunchRequest (the first one) then return true
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech = "Welcome to Voice Assistant Adventure, I will be your dungeon master.\n" \
                 "You begin in a musty dungeon cellar, what do you do?"
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard("Voice Assistant Adventure", "Welcome")).set_should_end_session(
            False)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # if the request is LaunchRequest (the first one) then return true
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        speech = "Thank you for playing voice assistant adventure."
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard("Good Bye", speech)).set_should_end_session(
            True)
        return handler_input.response_builder.response


class IntentRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # if the request is LaunchRequest (the first one) then return true
        # if had various intents, could do is_intent_name() instead.
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        data = parse_data(get_slot_value(handler_input, 'data'))
        speech = perform_action(data[0], data[1], data[2], data[3])
        handler_input.response_builder.speak(speech).set_should_end_session(
            False)
        return handler_input.response_builder.response



class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        # speech = "Could you say that again?"
        speech = exception.__str__()
        handler_input.response_builder.speak(speech)
        handler_input.response_builder.set_should_end_session(False)
        return handler_input.response_builder.response


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(IntentRequestHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(AllExceptionHandler())
