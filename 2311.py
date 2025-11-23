import numpy as np

# Định nghĩa ảnh 4x4
I = np.array([
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 2, 2, 2],
    [2, 2, 3, 3]
])

# Tham số
d = 1  # khoảng cách
theta = 0  # góc 0° (theo hàng, pixel bên phải)

def extract_pixel_pairs(image, distance, angle):
    """
    Trích xuất các cặp pixel theo khoảng cách và góc cho trước
    
    Args:
        image: Ma trận ảnh
        distance: Khoảng cách giữa các pixel
        angle: Góc (0°: theo hàng, pixel bên phải)
    
    Returns:
        List các tuple chứa cặp pixel (pixel_gốc, pixel_lân_cận)
    """
    pairs = []
    rows, cols = image.shape
    
    if angle == 0:  # Theo hàng, pixel bên phải
        for i in range(rows):
            for j in range(cols - distance):
                pixel1 = image[i, j]
                pixel2 = image[i, j + distance]
                pairs.append((pixel1, pixel2))
    
    return pairs

# Trích xuất các cặp pixel
pixel_pairs = extract_pixel_pairs(I, d, theta)

# Hiển thị kết quả
print("Ảnh gốc:")
print(I)
print(f"\nCác cặp pixel với d={d}, θ={theta}°:")
for i, pair in enumerate(pixel_pairs):
    print(f"Pair {i+1}: {pair}")

# Thống kê số lượng cặp
print(f"\nTổng số cặp pixel: {len(pixel_pairs)}")

# Tạo ma trận đồng xuất hiện (Co-occurrence Matrix)
gray_levels = [0, 1, 2, 3]
co_occurrence_matrix = np.zeros((len(gray_levels), len(gray_levels)), dtype=int)

for pair in pixel_pairs:
    i, j = pair
    co_occurrence_matrix[i, j] += 1

print(f"\nMa trận đồng xuất hiện (Co-occurrence Matrix):")
print("   ", end="")
for level in gray_levels:
    print(f"{level:3}", end="")
print()
for i, level_i in enumerate(gray_levels):
    print(f"{level_i}: ", end="")
    for j, level_j in enumerate(gray_levels):
        print(f"{co_occurrence_matrix[i, j]:3}", end="")
    print()