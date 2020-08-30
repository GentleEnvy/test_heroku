from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll


GROUP_ID = 187918549
GROUP_TOKEN = 'a0665e15baa72b932e05f2552524fb6fa90e6a5ae26a289d7879d7889db91a6ed60885d03a97e75e08679'

bot = VkApi(token=GROUP_TOKEN)
lp = VkBotLongPoll(bot, GROUP_ID)

for event in lp.listen():
    print(event)




# import os
#
# import dialogflow_v2.proto.context_pb2
# from dialogflow_v2 import SessionsClient
# from dialogflow_v2.proto.session_pb2 import TextInput, QueryInput, QueryParameters
#
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'private_key.json'
#
# DIALOGFLOW_PROJECT_ID = 'test-hdev'
# DIALOGFLOW_LANGUAGE_CODE = 'ru'
# SESSION_ID = '123'
#
# text_to_be_analyzed = "прив"
#
# session_client = SessionsClient()
# session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#
# text_input = TextInput(
#     text=text_to_be_analyzed,
#     language_code=DIALOGFLOW_LANGUAGE_CODE
# )
#
# query_input = QueryInput(
#     text=text_input
# )
#
# project_id = DIALOGFLOW_PROJECT_ID
# session_id = SESSION_ID
# context_id = 'call'
#
# query_params = QueryParameters(
#     contexts=[
#         dialogflow_v2.proto.context_pb2.Context(
#             name=f'projects/{project_id}/'
#                  f'agent/sessions/{session_id}/contexts/{context_id}',
#             lifespan_count=1
#         )
#     ]
# )
#
# import time
# st = time.time()
#
# response = session_client.detect_intent(
#     session=session,
#     query_input=query_input,
#     query_params=query_params
# )
#
# print(time.time() - st)
#
# print("Query text:", response.query_result.query_text)
# print("Detected intent:", response.query_result.intent.display_name)
# print("Detected intent confidence:", response.query_result.intent_detection_confidence)
# print("Fulfillment text:", response.query_result.fulfillment_text)
