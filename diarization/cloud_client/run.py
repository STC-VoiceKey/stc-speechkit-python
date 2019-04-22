import base64

from cloud_client import DiarizationApi, AudioDto, AuthRequestDto
from cloud_client.api.session_api import SessionApi

session_api = SessionApi()
credentials = AuthRequestDto("user", 261, "password")
session = session_api.login(credentials).session_id
session_api.check(session)
diarizationApi = DiarizationApi()
in_file = open("F:\\Cloud\\test\\ira_8khz.wav", "rb")
data = in_file.read()
in_file.close()
encoded_string = base64.standard_b64encode(data)
encoded_string = str(encoded_string, 'ascii', 'ignore')
diarization_param = AudioDto(encoded_string)
diarization_result = diarizationApi.diarization(session, diarization_param)
print(diarization_result)