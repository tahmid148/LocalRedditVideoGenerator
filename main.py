from tts.executeModel import create_synthesizer, generate_speech

syn = create_synthesizer()

generate_speech(syn, "some_file")