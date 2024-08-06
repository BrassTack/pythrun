# pythrun

`pythrun` is a lightweight Python script that automatically sets up a virtual environment, installs necessary dependencies, and runs your Python scripts. It is especially useful for quickly setting up and running prototype or early-stage scripts.

## Features

- **Automatic Virtual Environment Creation**: Creates a `.venv` directory in the script's directory.
- **Dependency Management**: Installs required dependencies based on imports in the script and a `requirements.txt` file, if present.
- **Script Execution**: Runs the specified Python script within the created virtual environment.

## Installation

No installation is needed. Just download `pythrun` and place it in the same directory as your Python script.

## Usage

To run a Python script using `pythrun`, navigate to the directory containing your script and run:

```sh
./pythrun <script.py> [script arguments...]
```

For example:

```sh
./pythrun my_script.py arg1 arg2
```

## How It Works

1. **Virtual Environment Creation**: If a virtual environment (`.venv`) does not exist in the script's directory, `pythrun` creates one.
2. **Dependency Installation**:
    - Checks for a `requirements.txt` file and installs listed dependencies.
    - Parses the script to identify imported modules and installs any missing ones.
3. **Script Execution**: Runs the specified script within the virtual environment, passing any provided arguments.

## Example

Given a script `example.py`:

```python
import requests

def main():
    response = requests.get('https://api.github.com')
    print(response.json())

if __name__ == "__main__":
    main()
```

Run it with:

```sh
./pythrun example.py
```

`pythrun` will:
- Create a virtual environment in the current directory.
- Install the `requests` library.
- Execute `example.py`.

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this software dedicate any and all copyright interest in the software to the public domain. We make this dedication for the benefit of the public at large and to the detriment of our heirs and successors. We intend this dedication to be an overt act of relinquishment in perpetuity of all present and future rights to this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss potential changes.

## Running the Test Tool

To ensure that the output works properly, you can use the provided test tool. Run the following command:

```bash
./pythrun pythrun-test.py
```
