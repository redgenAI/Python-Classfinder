# Class Finder

Class Finder is a simple utility script written in Python that helps users to find the module or submodule a particular class belongs to within a specified Python library. This tool can be useful when dealing with large or unfamiliar libraries.

## Motivation

When working with large or poorly documented libraries, finding where a particular class is defined can be like looking for a needle in a haystack. Class Finder aims to ease this process by programmatically searching through all submodules of a specified library to find where a class is defined.

## Getting Started

### Prerequisites

- Python 3.x
- I recommend you run this script from your target virtual environment. The script will check for the given library and install it if it is not found.
Usage

1. Clone this repository to your local machine:

   ```bash
   git clone 
   cd class-finder
   ```
2. Run the `classfinder.py` script:

   ```bash
   python classfinder.py
   ```
3. When prompted, enter the name of the library you wish to search through. If the library is not installed, the script will attempt to install it using pip.

   ```plaintext
   Enter the name of the library: some_library
   ```
4. Next, enter the name of the class you are looking for.

   ```plaintext
   Enter the name of the class you are looking for: SomeClass
   ```
5. The script will then search through all submodules of the specified library, and if the class is found, it will output the name of the module or submodule the class belongs to.

   ```plaintext
   SomeClass found in some_library.some_submodule
   ```

## Contributing

Feel free to fork this repository, create a feature branch, and submit a Pull Request if you have additions or fixes to contribute.

## License

This is open source.
