"""Helper Functions."""

import PyPDF2
import uuid
# import speech_recognition as sr


def generate_id():
    """Generate unique random ID."""
    unique_id = str(uuid.uuid4()).replace("-", "")
    return unique_id


def pdf2text(pdf_file):
    """Extract text from a PDF file."""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"


def is_enterKey(keyboardEvent):
    """Return True if just the Enter key is pressed.

    # keyboardEvent = {"key": "Enter", "altKey": false, "ctrlKey": false, "shiftKey": false, "metaKey": false, "repeat": false}
    """
    if keyboardEvent is None:
        return False
    if keyboardEvent["key"] == "Enter" and not keyboardEvent["shiftKey"]:
        return True
    return False


# def voice2text():
#     """Listen to audio input from a microphone and transcribes it into text."""
#     # Initialize the recognizer
#     recognizer = sr.Recognizer()

#     # Start the microphone input
#     with sr.Microphone() as source:
#         print("Please speak something...")
        
#         recognizer.pause_threshold=0.8
#         recognizer.phrase_time_limit=8 
#         #recognizer.operation_timeout=10
#         recognizer.instant_energy_threshold=300
#         recognizer.dynamic_energy_threshold=True
#         #recognizer.dynamic_energy_adjustment_ratio=1.5

#         # Adjust for ambient noise
#         recognizer.adjust_for_ambient_noise(source)
        
#         # Capture the audio
#         audio = recognizer.listen(source, timeout=3) 

#         text = ''
#         try:
#             # Recognize the speech using Google Web Speech API
#             text = recognizer.recognize_google(audio)
#         except sr.WaitTimeoutError as e:
#             print("Timeout; {0}".format(e))
#         except sr.UnknownValueError:
#             print("Sorry, I could not understand the audio.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#         except Exception as err:
#             print(f"other; {err}")

#         return text



# def do_upload_file(contents, filename):
#     # attached_file = {'data': None, 'icon': None}
#     attached_file = dict()
    
#     # image file
#     # if filename.lower().endswith((".png", ".jpg")):
#     #     return contents, "", ""
    
#     # pdf file
#     if filename.endswith(".pdf"):
#         if contents is not None: 
#             _, content_string = contents.split(',')
#             decoded_content = base64.b64decode(content_string)
#             pdf_file = io.BytesIO(decoded_content)
#         try:
#             text = uhf.pdf2text(pdf_file)
#             attached_file = {'data': text, 'icon': "/assets/images/pdf_icon.png"}
#             return uploaded_file_icon(attached_file['icon']), attached_file,  "", None
#         except Exception as e:
#             return uploaded_file_icon(), attached_file,  "", None

#     return uploaded_file_icon(), attached_file,  "", None
