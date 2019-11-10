from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type
from ask_sdk_model.ui import SimpleCard
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from .parsing.lambda_function import lambda_handler

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        # if the request is LaunchRequest (the first one) then return true
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):

        speech = "Welcome to Voice Assistant Adventure, I will be your dungeon master.\n" \
                 "You begin in a musty dungeon cellar, what do you do?"
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard("Voice Assistant Adventure", speech)).set_should_end_session(
            False)
        return handler_input.response_builder.response

class IntentRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # if the request is LaunchRequest (the first one) then return true
        # if had various intents, could do is_intent_name() instead.
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):

        # lda = lambda_handler(handler_input)

        # response = "Howdy neighbor"
        speech = "An interesting choice"

        #speech = lda["response"]

        handler_input.response_builder.speak(speech)
        handler_input.response_builder.set_card(SimpleCard("Awesome", speech))
        handler_input.response_builder.set_should_end_session(True)

        return handler_input.response_builder.response

class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        speech = "Could you say that again?"
        handler_input.response_builder.speak(speech)
        handler_input.response_builder.set_should_end_session(False)
        return handler_input.response_builder.response

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(IntentRequestHandler())
sb.add_exception_handler(AllExceptionHandler())
