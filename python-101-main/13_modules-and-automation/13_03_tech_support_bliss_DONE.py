# Use the built-in `platform` module to print out the following info:
import platform

placeholder = "remove me :)"

plataform = platform.platform()
compiler = platform.python_compiler()
version = platform.python_version()
system = platform.system()
release = platform.release()
processor = platform.processor()

print(f"{'Platform:':>10} {plataform}",)  # platform.platform()
print(f"{'Compiler:':>10} {compiler}",)  # platform.python_compiler()
print(f"{'Python:':>10} {version}",)  # platform.python_version()
print(f"{'System:':>10} {system}",)  # platform.system()
print(f"{'Release:':>10} {release}",)  # platform.release()
print(f"{'System:':>10} {processor}",)  # platform.processor()

