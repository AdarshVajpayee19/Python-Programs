class A:
    def show(self):
        print("In A Show")


class B(A):
    """
    def show(self):
        print("In B Show")
    """
    pass

s1 = B()
s1.show() # In A Show when we use Pass
s1.show() # In B show When we use def show method of Class B.
