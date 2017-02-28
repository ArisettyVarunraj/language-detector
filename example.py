from src.detection import get_closest_language as DetectLanguage

text_trk = "Bu Türkçe bir kelimedir"
print(DetectLanguage(text_trk))

text_eng = "This is an English word"
print(DetectLanguage(text_eng))
