def print_triforce(n: int):
  central_axis = 2 * n

  for i in range(1, n + 1):
    triangle = "*" * (2 * i - 1)
    centered_triangle = triangle.center(central_axis * 2)
    print(centered_triangle)

  for i in range(1, n + 1):
    triangle = "*" * (2 * i - 1)
    centered_triangle = triangle.center(central_axis)
    duplicated_triangle = centered_triangle * 2
    print(duplicated_triangle)


def main():
  triforce_level = int(input("Enter the triforce level: "))
  print_triforce(triforce_level)  

if __name__ == "__main__":
  main()
