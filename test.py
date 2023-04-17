from app import app

'''
   This is a simple status code test script
'''
########################################## Home Page ################################################
def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200

######################################### ChatGPT Bot ###############################################
def test_chatbot():
   response = app.test_client().get('/gpt')
   assert response.status_code == 200

def test_chatbot1():
   response = app.test_client().get('/gpt1')
   assert response.status_code == 200

######################################### YouTube Downloader ########################################
def test_downloader():
   response = app.test_client().get('/download')
   assert response.status_code == 200

##################################### Youtube Transcribe ############################################
def test_transcript():
   response = app.test_client().get('/transcript')
   assert response.status_code == 200

# def test_transcript1():
#    response = app.test_client().get('/transcript1')
#    assert response.status_code == 200