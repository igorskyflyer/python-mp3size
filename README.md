# mp3size - Python

🎶 `Mp3Size` - calculates an estimated file size of Mp3 files, now in Python! 🎯

🧮 Calculates an estimated file size of Mp3 files. 🎶

Usage
A simple usage example:

```python
import mp3size

def main():
    print(mp3size.getFileSize("03:30"))  # returns 4200
    print(mp3size.getFileSize("03:18", 320))  # returns 7920
    print(mp3size.getAudioDuration(6474, 306))  # returns 00:02:49
    print(mp3size.getAudioBitrate("03:42", 5346))  # returns 192
```
