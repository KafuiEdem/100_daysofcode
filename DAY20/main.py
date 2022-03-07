class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    
    def breathe(sel):
        print('inhale,exhale')

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(sel):
        super().breathe()
        print('doing this under water')

    def swim(self):
        print('moving in water')

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)