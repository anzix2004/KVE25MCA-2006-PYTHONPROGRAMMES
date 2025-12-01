import graphis.rectangle
import graphis.circle
import graphis.graphics_3d.cuboid as cub 
import graphis.graphics_3d.sphere as sph

print("Rectangle Area:", graphis.rectangle.area(10, 5))

print("Rectangle Area:", graphis.rectangle.perimeter(10, 5))

print("Circle Perimeter:", graphis.circle.perimeter(3))
print("Circle Perimeter:", graphis.circle.area(3))
print("Cuboid Area:", cub.area(2, 3, 4))
print("Sphere Area:", sph.area(6))
print("Cuboid Area:", cub.perimeter(2, 3, 4))
print("Sphere Area:", sph.perimeter(6))
