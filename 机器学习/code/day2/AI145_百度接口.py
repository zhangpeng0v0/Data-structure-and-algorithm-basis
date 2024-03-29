from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '15648240'
API_KEY = '8aewbMjPk6k7b1EQVCgaMt7U'
SECRET_KEY = 'dOG550wgoCyQibLEeS6M98G0vEmLXqUZ'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
# 识别本地文件
resp=client.asr(get_file_content('test.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})
# 语音合成
result  = client.synthesis('床前明月光，地上鞋两双', 'zh', 1, {
    'vol': 15,'spd':5,'pit':5,'per':1
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)