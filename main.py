from PIL import Image
import whisper
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import string

model = whisper.load_model("base")
alph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def get_indices(word_list):
    indices_list = []

    for word in word_list:
        indices = []
        for letter in word:
            if letter.isalpha():
                indices.append(alph.index(letter))
        indices_list.append(indices)

    return indices_list


def clean_string(input_string):
    word_list = input_string.split()
    word_list = [word.translate(str.maketrans('', '', string.punctuation)) for word in word_list]
    word_list = [word.lower() for word in word_list]
    return word_list



result = model.transcribe("hellothere.mp3")
transcribedText = result["text"]
print(transcribedText)
words = clean_string(transcribedText)
print(words)

numsListToDisplay = get_indices(words)
print(numsListToDisplay)
for word in numsListToDisplay:
    for l in word:
        letter = mpimg.imread('aslImages/' + str(l) + '.png')
        plt.figure()
        plt.imshow(letter)
        print("space")

plt.show()
plt.close()
