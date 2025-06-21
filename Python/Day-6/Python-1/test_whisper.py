import whisper
import os

def get_text_from_media(FILE_URL):
    """This function extracts text from media"""
    model = whisper.load_model("base")

    transcript = model.transcribe(FILE_URL)
    transcribed_text = transcript['text']

    directory_path = "/transcribed_text"
    file_path = os.path.join(directory_path, "transcript.txt")

    # if not os.path.exists(directory_path):
    #     os.makedirs(directory_path)

    with open(file_path, 'w') as file:
        file.write(transcribed_text)
        
    return transcribed_text

if __name__ == "__main__":
    FILE_URL = "/home/shtlp_0015/Downloads/Months/1st month/Python/Day-1/Python-1/taking_a_genetic_family_history__the_pedigree_(sudden_death) (540p).mp4"

    get_text_from_media(FILE_URL)