from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type
from ask_sdk_core.utils import get_slot_value
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
        """temp_json = {
            "version": "1.0",
            "session": {
                "new": False,
                "sessionId": "amzn1.echo-api.session.b43f80d4-496b-40d2-ab66-df0b2f237229",
                "application": {
                    "applicationId": "amzn1.ask.skill.4a273731-5750-4824-aa1b-383b3be3f5ca"
                },
                "user": {
                    "userId": "amzn1.ask.account.AG4UZ2MCEOYQ74DKFPSACD2SUYBUXWIWLGK43UHOHPPBRRFCJ6H2SJBCEIMXOYYQ5BYGLPS6DP3XKBCS4HZBF3VAU43C6SMTYWNRTVZIOAV3ZYDKZY4JUFZPRLZ53AL563OAKIIMZVO2BSBLIGO4Q4TNYO3SBFVXETMNTWR3WUKVVC6YJ6RAWGCQXPXLUCFMJWHFXHU4WNYC6RY"
                }
            },
            "context": {
                "System": {
                    "application": {
                        "applicationId": "amzn1.ask.skill.4a273731-5750-4824-aa1b-383b3be3f5ca"
                    },
                    "user": {
                        "userId": "amzn1.ask.account.AG4UZ2MCEOYQ74DKFPSACD2SUYBUXWIWLGK43UHOHPPBRRFCJ6H2SJBCEIMXOYYQ5BYGLPS6DP3XKBCS4HZBF3VAU43C6SMTYWNRTVZIOAV3ZYDKZY4JUFZPRLZ53AL563OAKIIMZVO2BSBLIGO4Q4TNYO3SBFVXETMNTWR3WUKVVC6YJ6RAWGCQXPXLUCFMJWHFXHU4WNYC6RY"
                    },
                    "device": {
                        "deviceId": "amzn1.ask.device.AEC3JFD62KVWNBHSSTGK4EZKCLG5TLJ2RMKSD4IXPBB6NTNOCTAMW6BBD3464PDQZHJQBGSIZUWMCXL3RGOUXK7YLIPVBC7ZVKZFG7YAK53XHJYXQQ76ALF4BKO3YB5FWL2YAHOFZI7MLHT4U5ZEWLNHWLDO4ZJ4IVLMVG7BNYRSJEVWAIGEE",
                        "supportedInterfaces": {}
                    },
                    "apiEndpoint": "https://api.amazonalexa.com",
                    "apiAccessToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjEifQ.eyJhdWQiOiJodHRwczovL2FwaS5hbWF6b25hbGV4YS5jb20iLCJpc3MiOiJBbGV4YVNraWxsS2l0Iiwic3ViIjoiYW16bjEuYXNrLnNraWxsLjRhMjczNzMxLTU3NTAtNDgyNC1hYTFiLTM4M2IzYmUzZjVjYSIsImV4cCI6MTU3MzM3ODQ4MywiaWF0IjoxNTczMzc4MTgzLCJuYmYiOjE1NzMzNzgxODMsInByaXZhdGVDbGFpbXMiOnsiY29udGV4dCI6IkFBQUFBQUFBQUFDcStVcDR3aXpRZmdaVjcxMjRhZmF6S2dFQUFBQUFBQUNTRUowL2FyR2JFaW9ZdFZJc3pnQmRZMkpKcnMzS2F1SEt3cU9ZN1FJT0t2WGNleXd5SGhWR3ZlMHk5M0MzMXBCLzBRRUJqZWhWczZNOUEwOFd3ZTRYMGxScWUwV0k3RWhGSkZDRnF1SHkzTGdFNUlvNmhxYXRDZmp2ZitOVkhvVlRIZkZVb0lNS1FHeE9rN200ZG5sbDdHcmxiTk1lVjJ4MEpPKzdKUGJHM3hzaUNpR1hKSVVzVm5FNXVjdFV1QlFrZjhWZmZxUzNURE8yYlI4eTc5N01oQ05CYnczTE5ic2lxWnVJNjdLRVk5anJLVk5FQkVldS83QVU2d0dCUGowU3JzT1luR3RsRGlaL0d1aDUyK2M1NnRHeGI3WHdSTWFtTVRwLzNtcUJVZlNaVmFmODlzSXpVdUxIZVAveTBLRnpEN3M1WmxHR3U4MEx3dVVpclZjOS9HREJESG9zRlJNRlJqTWFwY0t6ZjM3T2trUHBvdkkxS0RlcTBPWE82WDVqRzFzYk9wVC9sVjFtIiwiY29uc2VudFRva2VuIjpudWxsLCJkZXZpY2VJZCI6ImFtem4xLmFzay5kZXZpY2UuQUVDM0pGRDYyS1ZXTkJIU1NUR0s0RVpLQ0xHNVRMSjJSTUtTRDRJWFBCQjZOVE5PQ1RBTVc2QkJEMzQ2NFBEUVpISlFCR1NJWlVXTUNYTDNSR09VWEs3WUxJUFZCQzdaVktaRkc3WUFLNTNYSEpZWFFRNzZBTEY0QktPM1lCNUZXTDJZQUhPRlpJN01MSFQ0VTVaRVdMTkhXTERPNFpKNElWTE1WRzdCTllSU0pFVldBSUdFRSIsInVzZXJJZCI6ImFtem4xLmFzay5hY2NvdW50LkFHNFVaMk1DRU9ZUTc0REtGUFNBQ0QyU1VZQlVYV0lXTEdLNDNVSE9IUFBCUlJGQ0o2SDJTSkJDRUlNWE9ZWVE1QllHTFBTNkRQM1hLQkNTNEhaQkYzVkFVNDNDNlNNVFlXTlJUVlpJT0FWM1pZREtaWTRKVUZaUFJMWjUzQUw1NjNPQUtJSU1aVk8yQlNCTElHTzRRNFROWU8zU0JGVlhFVE1OVFdSM1dVS1ZWQzZZSjZSQVdHQ1FYUFhMVUNGTUpXSEZYSFU0V05ZQzZSWSJ9fQ.iqiSpE0E8jEsSOZMh0u23ubFboqkpL0LLc23tRoGp4tJmHpzJU7y7HmSz_YJFTVOWP8SXMxldzYyngHNldAXM7RUm3TK1Aa2XVSCaOif4gm3Qi1uQW3QruYEvsoGNH7nk4UDASj5p3Kj1jUil6Cx228-JGAOT3Gfz_fPFHM3mi8GvI62Ac28lor_NR6gG141YSs0zTxADcQvC7ro61K4Ag0jB8vsnXpSKsKgsSjmDgXsP2MxNrQUg-3vyxxxPLg_tDxAnP3tUVJFY0QihkOSAXiAJj5SX6j6r97FECgqtA98FX490aclczRoYeoXK_3TeqT1W3LxUbujHWR9NJx5Mg"
                },
                "Viewport": {
                    "experiences": [
                        {
                            "arcMinuteWidth": 246,
                            "arcMinuteHeight": 144,
                            "canRotate": False,
                            "canResize": False
                        }
                    ],
                    "shape": "RECTANGLE",
                    "pixelWidth": 1024,
                    "pixelHeight": 600,
                    "dpi": 160,
                    "currentPixelWidth": 1024,
                    "currentPixelHeight": 600,
                    "touch": [
                        "SINGLE"
                    ],
                    "video": {
                        "codecs": [
                            "H_264_42",
                            "H_264_41"
                        ]
                    }
                },
                "Viewports": [
                    {
                        "type": "APL",
                        "id": "main",
                        "shape": "RECTANGLE",
                        "dpi": 160,
                        "presentationType": "STANDARD",
                        "canRotate": False,
                        "configuration": {
                            "current": {
                                "video": {
                                    "codecs": [
                                        "H_264_42",
                                        "H_264_41"
                                    ]
                                },
                                "size": {
                                    "type": "DISCRETE",
                                    "pixelWidth": 1024,
                                    "pixelHeight": 600
                                }
                            }
                        }
                    }
                ]
            },
            "request": {
                "type": "IntentRequest",
                "requestId": "amzn1.echo-api.request.b2ea4ce0-8797-4755-844c-66055955b020",
                "timestamp": "2019-11-10T09:29:43Z",
                "locale": "en-US",
                "intent": {
                    "name": "takeAction",
                    "confirmationStatus": "NONE",
                    "slots": {
                        "data": {
                            "name": "data",
                            "value": "attack",
                            "confirmationStatus": "NONE",
                            "source": "USER"
                        }
                    }
                }
            }
        }
        """
        # return lambda_handler(temp_json)
        speech = get_slot_value(handler_input, 'data')
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
