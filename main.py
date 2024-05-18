from PIL import Image
# import matplotlib.pyplot as plt
import whisper
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = whisper.load_model("base")

result = model.transcribe("hellothere.mp3")
transcribedText = result["text"]
print(transcribedText)


img = mpimg.imread('aslImages/0.png')
plt.imshow(img)
plt.show()
