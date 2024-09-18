class Bird:
    def fly(self):
        return 'Bird is flying...!'
class Parrot(Bird):
    def fly(self):
        return 'It is Parrot:)'
class crow(Bird):
    def fly(self):
        return 'It is Crow:)'
def test_fly(bird):
    print(bird.fly())
b1=Bird()
p1=Parrot()
c1=crow()
print(b1.fly())
print(p1.fly())
print(c1.fly())
