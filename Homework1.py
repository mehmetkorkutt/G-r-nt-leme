import cv2

image = cv2.imread('C:\\Users\\korku\\PycharmProjects\\HW1\\bottle.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

height, width = thresh.shape
bottle_width = width // 5  # Şişe sayısı 5 olduğu için genişliği 5'e böldük

white_pixel_counts = []
for i in range(5):

    bottle_region = thresh[:, i * bottle_width:(i + 1) * bottle_width]

    white_pixels = cv2.countNonZero(bottle_region)
    white_pixel_counts.append(white_pixels)

different_bottle_index = white_pixel_counts.index(min(white_pixel_counts))
print(f"Farklı olan şişe: {different_bottle_index + 1}. sıradaki şişe")
