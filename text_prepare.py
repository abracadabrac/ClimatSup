import re
import unicodedata


def text_prepare(text):

    if type(text) is not str:
        return text

    if text[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        # need to be donne
        return text

        text = re.sub(',', '.', text)
        text = re.sub(re.compile('[^0-9 +]'), '', text)
        text = float(text)

        return text

    #text = text.lower()  # lowercase text
    text = re.sub(re.compile('[/(){}\[\]\|@,;]'), ' ', text)
    text = re.sub(re.compile('[éèê]'), 'e', text)
    text = re.sub(re.compile('[âä]'), 'a', text)
    text = re.sub(re.compile('[îï]'), 'i', text)
    text = re.sub(re.compile('[ù]'), 'u', text)
    text = re.sub(re.compile('[^0-9a-zA-Z #+_ +]'), '', text)
    text = re.sub(re.compile(r"[^\S\n\t]+$"), '', text)
    text = re.sub(re.compile(' +'), ' ', text)
    text = re.sub(' ', '_', text)

    return text


if __name__ == '__main__':
    print(text_prepare('je suis fière de toi mon    AaAaAaAabbBBBbBBB  amie hééé HHH    ^^ùù@&ÉR"§È!ÉÇÀ    '))
