class MyClass (object):
    pass 

my_instance =MyClass()
MyClass.class_attribute = 'hello' 
my_instance.instance_attribute = 'world' 
dir(my_instance)
['__class__', ... , 'class_attribute', 'instance_attribute']
print(my_instance.__class__)

print(my_instance.instance_attribute)
print(my_instance.class_attribute)
print(MyClass.instance_attribute)

Traceback (most recent call last):
    File"<pyshell#11>", line1, in <module> 
        print MyClass.instance_attribute
AttributeError: type object 'MyCLass' has no attribute 'instance_attribute'