# Import Modules
from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

def create_synthesizer():
    # Provide path for model manager JSON file
    path = "/home/tahmid/.local/lib/python3.10/site-packages/TTS/.models.json"

    # Initialise Model Manager
    model_manager = ModelManager(path)

    print("Downloading Models...")
    # Download TTS model and its associated vocoder
    model_name = "tts_models/en/jenny/jenny"
    model_path, config_path, model_item = model_manager.download_model(model_name)

    print("Creating Synthesizer...")
    # Create a Synthesizer instance
    return Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
    )

def generate_speech(syn, input, output_name):
    print("Converting text...")
    # Synthesize speech from text
    output = syn.tts(input)

    print("Saving output file...")
    # Save the generated speech as an audio file
    syn.save_wav(output, f"output/{output_name}.wav" )