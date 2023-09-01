# Import Modules
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

# Provide path for model manager JSON file
path = "/home/tahmid/.local/lib/python3.10/site-packages/TTS/.models.json"

# Initialise Model Manager
model_manager = ModelManager(path)

print("Downloading Models...")
# Download TTS model and its associated vocoder
model_name = "tts_models/en/jenny/jenny"
model_path, config_path, model_item = model_manager.download_model(model_name)
# vocoder_name = "vocoder_models/en/ljspeech/univnet"
# voc_path, voc_config_path, _ = model_manager.download_model(vocoder_name)


print("Creating Synthesizer...")
# Create a Synthesizer instance
syn = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
    # vocoder_checkpoint=voc_path,
    # vocoder_config=voc_config_path
)

# Text to be converted into speech
text_input_path = "input.txt"
with open(text_input_path, "r", encoding="utf-8") as file:
    text = file.read()
    
print("Converting text...")
# Synthesize speech from text
outputs = syn.tts(text)

print("Saving output file...")
# Save the generated speech as an audio file
syn.save_wav(outputs, "output/audio.wav")

print("Done")