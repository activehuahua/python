from classes.models.count import A


class B(A):
    def sub(self, a, b):
        return a - b


result = B().add(2, 5)
print(result)
result = B().sub(5, 2)
print(result)
