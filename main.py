from tts.executeModel import create_synthesizer, generate_speech

syn = create_synthesizer()

generate_speech(syn, "Hi my name is billy", "some_other_file")