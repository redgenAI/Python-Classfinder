import importlib
import pkgutil
import subprocess

def find_class_in_submodules(library_name, class_name):
    library = importlib.import_module(library_name)

    for loader, submodule_name, is_pkg in pkgutil.walk_packages(library.__path__):
        full_submodule_name = f"{library_name}.{submodule_name}"
        try:
            submodule = importlib.import_module(full_submodule_name)
            if class_name in dir(submodule):
                return full_submodule_name
        except ImportError:
            pass

    return None

def main():
    library_name = input("Enter the name of the library: ").strip()
    class_name = input("Enter the name of the class you are looking for: ").strip()

    try:
        importlib.import_module(library_name)
    except ImportError:
        print(f"{library_name} is not installed. Installing now...")
        subprocess.run(["pip", "install", library_name])

    result = find_class_in_submodules(library_name, class_name)
    if result:
        print(f'{class_name} found in {result}')
    else:
        print(f'{class_name} not found in any submodules of {library_name}')

if __name__ == "__main__":
    main()