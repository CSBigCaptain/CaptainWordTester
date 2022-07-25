# CSBigCaptain's Word Tester

## About

The tester is a simple and weak word tester. But it will get stronger as I grow up!

The program was made in Python 3.10.5 (Microsoft Store Edition).

## How to use

- If you want to use the word tester, you must make sure your PC has a Python environment. About how to install Python: this is not within the technical limits of this readme document.

To run the program, input this piece of code into shells like, for example, `cmd` and `powershell`.
  ```powershell
  python main.py
  ```

**<u>Warning: You must make sure these Python files and two Datas folder are in the same path. Instead, the program may have unexcepted bugs!</u>**

- About the MainFile :
  - The Datas folders (including `TxtDatas` and `JsonDatas`) are used to store questions that you have been asked.And they must be in the "Datas" folder. Without these files, or if the file path has problems, the program may report an error (as the time used for development is so short, we can't make sure it will report an error 100%).
  - The program has the JSON mode and the TXT mode. The txt mode uses the `TxtDatas/MainFile.txt` file and the json mode uses the `JsonDatas/MainFile.json` file. Editing the txt file is easy, but keeping the format right and streamlining is a bit difficult. Maybe the little format mistake in a superbly large txt file could make you superbly sad, and it is difficult to group words. As a result, I recommend that you use the json mode. Although editing a JSON file is difficult and troublesome, the JSON mode supports nested dictionaries, which the TXT mode cannot do.
  - <u>**Json mode warning: If a dictionary contains both words and other types of data, the program will automatically skip the other types of data and keep the dictionary when reading it.**</u>

## Plans in the future

The project's development has been stopped as I have to study in school. But I still collect the advice and bugs of the program. If you discover any bugs or have any suggestions, I would be most welcome to open an issue!

I plan to restart development on the program in June and release the first version in August.

Thanks, and enjoy the project!

</br>
CSBigCaptain
2022.4.18 in China
