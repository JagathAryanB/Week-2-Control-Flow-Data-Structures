from rapidocr_onnxruntime import RapidOCR
from pathlib import Path

img_path = Path(r'c:\devolopers arena\Week-2-Control-Flow-Data-Structures\week2Task.jpeg')
ocr = RapidOCR()
result, _ = ocr(str(img_path))
print('TEXT_COUNT', len(result or []))
if result:
    for item in result:
        print(f"{item[1]} || {item[2]}")
else:
    print('NO_TEXT_FOUND')
