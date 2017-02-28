# About
This is a basic language detector. It is comparing language profiles distance. The implementation is based on [here](https://www.let.rug.nl/~vannoord/TextCat/textcat.pdf).

# Dataset
Datasets were taken from [here](http://www.ohchr.org/EN/UDHR/Pages/SearchByLang.aspx).

# Usage

```python
from src.detection import get_closest_language as DetectLanguage

text_trk = "Bu Türkçe bir kelimedir"
print(DetectLanguage(text_trk))

text_eng = "This is an English word"
print(DetectLanguage(text_eng))
```

## Language
The default languages are **Turkish, English, Russian, German, French and Japanese** If you want to analyse more language, you just need to add random article to dataset directory.
