import collections


Anteater = collections.namedtuple('Anteater', ['weight', 'velocity', 'age'])


def print_anteater(anteaters):
    'Print anteaters weight and velocity' 
    print('This anteater weighs ' + str(anteater.weight) + 'and moves ' + str(anteater.velocity))

anteaters_weights = [ 50, 60, 70, 80]
anteaters_velocity = [ 100, 200, 300, 400]
anteaters_list = [Anteater (50, 100),
                  Anteater (60, 200),
                  Anteater (70, 300),
                  Anteater (80, 400)]

for anteater in anteaters_list:
    if anteater.weight%20 == 0:
        print_anteater(anteater)
    else:
        print("Anteater is NOT divisible by 20")

mass = 50
velocity = 15
print( 1 / 2 * mass * velocity ** 2)


# y = mx + b
# y = 1/2 *  x + 3
# f(x, y, z) = 1/2 * x + 3
def kinetic_energy(mass, velocity) -> float:
    kinetic_energy = 1 / 2 * mass * velocity ** 2
    return kinetic_energy
