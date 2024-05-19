import streamlit as st
import whisper


st.title("Transcribe Meetings")

# upload audio with streamlit
audio_file = st.file_uploader("Upload audio", type=["wav", "mp3", "m4a"])

@st.cache # Why dow you cache a model?
def load_whisper_model():
    model = whisper.load_model("base")
    return model

model = load_whisper_model()
# if st.sidebar.button("Load Whisper Model"):
#     model = load_whisper_model()
#     st.sidebar.success("Whisper model loaded.")

if st.sidebar.button("Transcribe Audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing audio")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription succeeded.")
        text = st.markdown(transcription["text"])
    else:
        st.sidebar.error("Please, upload an audio file.")


st.sidebar.header("Play Original Audio File")
st.sidebar.audio(audio_file)
