from feature_files.dadjoke import dadjoke
from feature_files.GoogleSearch import GoogleSearch
from feature_files.text_summarizer import summary

class Assistant():
    def __init__(self, name):
        self.name = name

    def dadjoke(self):
        return dadjoke()

    def GoogleSearch(self, query):
        return GoogleSearch(query)

    def summarize_text(self, text):
        return summary(text)
