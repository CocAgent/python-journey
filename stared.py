# Pattern Printer 🎨

def print_triangle(n, char):
    for i in range(1, n + 1):
        for j in range(i):
            print(char, end="")
        print()

def print_diamond(n, char):
    if n % 2 == 0:
        n += 1
    mid = n // 2
    for i in range(n):
        if i <= mid:
            spaces = mid - i
            chars = 2 * i + 1
        else:
            spaces = i - mid
            chars = 2 * (n - 1 - i) + 1
        print(" " * spaces + char * chars)

def print_pine_tree(n, char):
    for i in range(1, n + 1):
        spaces = n - i
        chars = 2 * i - 1
        print(" " * spaces + char * chars)
    
    trunk_width = 3 if n >= 3 else 1
    trunk_height = 1
    spaces = n - (trunk_width // 2) - 1
    for _ in range(trunk_height):
        print(" " * spaces + "|" * trunk_width)

def print_spiral(n, char):
    grid = [[" " for _ in range(n)] for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            grid[top][i] = char
        top += 1
        
        for i in range(top, bottom + 1):
            grid[i][right] = char
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                grid[bottom][i] = char
            bottom -= 1
            
        if left <= right:
            for i in range(bottom, top - 1, -1):
                grid[i][left] = char
            left += 1

    for row in grid:
        print(" ".join(row))

def main():
    while True:
        print("\n=== PATTERN PRINTER 🎨 ===")
        print("1. Tam giác")
        print("2. Kim cương")
        print("3. Cây thông")
        print("4. Spiral")
        print("5. Thoát")
        
        choice = input("Chọn hoa văn (1-5): ")
        
        if choice == '5':
            print("Tạm biệt!")
            break
            
        if choice in ['1', '2', '3', '4']:
            n = int(input("Nhập kích thước (n): "))
            char = input("Nhập ký tự tùy chọn (mặc định '*'): ") or "*"
            print()
            
            if choice == '1':
                print_triangle(n, char)
            elif choice == '2':
                print_diamond(n, char)
            elif choice == '3':
                print_pine_tree(n, char)
            elif choice == '4':
                print_spiral(n, char)
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

if __name__ == "__main__":
    main()