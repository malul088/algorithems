import cv2
import numpy as np

def manual_hsv(r, g, b):
    rn, gn, bn = r/255.0, g/255.0, b/255.0
    v = max(rn, gn, bn)
    c_min = min(rn, gn, bn)
    delta = v - c_min

    if delta == 0: return 0, 0, v  # מניעת חלוקה ב-0

    if v == rn: h = 60 * ((gn - bn) / delta)
    elif v == gn: h = 120 + 60 * ((bn - rn) / delta)
    else: h = 240 + 60 * ((rn - gn) / delta)
    
    if h < 0: h += 360 # תיקון זווית שלילית
    s = delta / v
    return h, s, v

def manual_hsl(r, g, b):
    rn, gn, bn = r/255.0, g/255.0, b/255.0
    v = max(rn, gn, bn)
    c_min = min(rn, gn, bn)
    delta = v - c_min
    l = (v + c_min) / 2

    if delta == 0: return 0, 0, l # מניעת חלוקה ב-0

    if v == rn: h = 60 * ((gn - bn) / delta)
    elif v == gn: h = 120 + 60 * ((bn - rn) / delta)
    else: h = 240 + 60 * ((rn - gn) / delta)
    
    if h < 0: h += 360
    s = delta / (1 - abs(2 * l - 1))
    return h, s, l

def manual_ycrcb(r, g, b):
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cr = (r - y) * 0.713 + 128
    cb = (b - y) * 0.564 + 128
    return y, cr, cb

def opencv_all_conversions(r, g, b):
    pixel = np.uint8([[[b, g, r]]])
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
    hls = cv2.cvtColor(pixel, cv2.COLOR_BGR2HLS)[0][0]
    ycrcb = cv2.cvtColor(pixel, cv2.COLOR_BGR2YCrCb)[0][0]
    return hsv, hls, ycrcb

# קלט
r = int(input("Enter Red (0-255): "))
g = int(input("Enter Green (0-255): "))
b = int(input("Enter Blue (0-255): "))

# חישובים
h_hsv, s_hsv, v_hsv = manual_hsv(r, g, b)
h_hsl, s_hsl, l_hsl = manual_hsl(r, g, b)
y_m, cr_m, cb_m = manual_ycrcb(r, g, b)
cv_hsv, cv_hls, cv_ycrcb = opencv_all_conversions(r, g, b)

# הדפסה
print("\n--- Manual Results ---")
print(f"HSV:   H={h_hsv:.1f}, S={s_hsv:.2f}, V={v_hsv:.2f}")
print(f"HSL:   H={h_hsl:.1f}, S={s_hsl:.2f}, L={l_hsl:.2f}")
print(f"YCrCb: Y={y_m:.1f}, Cr={cr_m:.1f}, Cb={cb_m:.1f}")

print("\n--- OpenCV Results ---")
print(f"HSV (H,S,V):   {cv_hsv}")
print(f"HLS (H,L,S):   {cv_hls}")
print(f"YCrCb (Y,Cr,Cb): {cv_ycrcb}")
