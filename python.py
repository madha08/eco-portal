data = [64,25,12,22,11]
# def swap(numbers, i, j):
#     numbers[i], numbers[j] = numbers[j], numbers[i]
# def bubble_pass(numbers, size):
#     for i in range(size -1):
#         if numbers[i] > numbers[i+1]:
#             swap(numbers, i, i+1)
# bubble_pass(data, 5)
# print(data)
# bubble_pass(data, 4)
# print(data)
# bubble_pass(data, 3)
# print(data)
# bubble_pass(data, 2)
# print(data)

def swap(data,i,j):
    data[i], data[j] = data[j], data[i]
def insert_element(data,index):
    i=index
    while i>0 and data[i-1]>data[i]:
        swap(data, i, i-1)
        i=i-1




def swap(data,i,j):
    data[i],data[j] = data[j],data[i]
def insert_element(data,index):
    i=index
    while i>0 and data[i-1]>data[i]:
        swap(data, i, i-1)
        i=i-1
    return data

for i in range (len(data)):
    print(insert_element(data,i))
