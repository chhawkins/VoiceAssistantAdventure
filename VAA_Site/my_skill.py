from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type
from ask_sdk_model.ui import SimpleCard
from ask_sdk_core.dispatch_components import AbstractExceptionHandler


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for skill launch."""
    def can_handle(self, handler_input):
        # if the request is LaunchRequest (the first one) then return true
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):

        speech = "If I say this you should be shitting your pants"
        handler_input.response_builder.speak(speech).set_card(
            SimpleCard("Holy Crap!", speech)).set_should_end_session(
            False)
        return handler_input.response_builder.response

class IntentRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        # if the request is LaunchRequest (the first one) then return true
        # if had various intents, could do is_intent_name() instead.
        return is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        speech = "I am replying to your intent and ending the session."

        print("HANDLER INPUT PRINT\n:",handler_input)


        handler_input.response_builder.speak(speech).set_card(
            SimpleCard("Awesome", speech)).set_should_end_session(
            True)
        return handler_input.response_builder.response

class AllExceptionHandler(AbstractExceptionHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        speech = "Sorry can you speak up asshole."
        handler_input.response_builder.speak(speech)
        return handler_input.response_builder.response

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(IntentRequestHandler())
sb.add_exception_handler(AllExceptionHandler())
