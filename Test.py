from pororo import Pororo

IMAGE_PATH = "/app/assets/images/단호박죽_1.jpg"
ocr = Pororo(task="ocr", lang="ko")
result = ocr(IMAGE_PATH)
print(result)
