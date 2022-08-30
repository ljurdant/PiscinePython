from vector import Vector
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print("v1.shape =",v1.shape)
print("v1.T() =",v1.T())

v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print("v3.dot(v4) =",v3.dot(v4))
print("v3+v4 =",v3+v4)