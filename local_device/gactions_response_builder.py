
## Resources: https://developers.google.com/actions/reference/conversation#http-response


def extractText(data):
    return data["inputs"][0]["raw_inputs"][0]["query"]

class GResponse:

    def __init__(self, conversation_token="", \
                 expect_user_response=False, \
                 text="", \
                 no_input_prompts=["Hmm Sorry, my fault. Try something else"]):
        self.conversation_token = conversation_token
        self.expect_user_response = bool(expect_user_response)
        self.text_to_speech = text
        self.no_input_prompts = no_input_prompts

    def _build_response(self):
        resp = {"conversation_token": self.conversation_token,\
                "expect_user_response": self.expect_user_response}
        if self.expect_user_response == False:
            resp["final_response"] = {"speech_response": \
                                      {"text_to_speech": self.text_to_speech}}
        else:
            resp["expected_inputs"] = [\
                {"input_prompt": {}, \
                 "possible_intents": [{"intent": "assistant.intent.action.TEXT"}]\
                 }]

            resp["expected_inputs"][0]["input_prompt"] = {
                        "initial_prompts": [
                          {"text_to_speech": self.text_to_speech}
                                            ],
                         "no_input_prompts" : [
                  {"text_to_speech": s} for s in self.no_input_prompts]
                        }

        return resp


    def __repr__(self):

        return str(self._build_response())

    def getJson(self):
        return self._build_response()



if __name__ == "__main__":

    r = GResponse(expect_user_response=True)
    print r
