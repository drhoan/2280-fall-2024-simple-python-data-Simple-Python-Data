import math
#write a function that compute the area of a circle
def compute_area(r):
    # put your code here
    return math.pi*r**2

if __name__ == "__main__":
    radius = int(input('Enter radius: '))
    print(f'The area is {compute_area(radius)}')