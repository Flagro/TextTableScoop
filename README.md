# 📝 ProjectText

Welcome to `ProjectText` 🌟, a versatile tool designed for extracting text from files and CSV tables, particularly focusing on Office files like Excel, PowerPoint, etc. This project is part of a suite that includes [`ProjectTextAgent`](https://github.com/Flagro/ProjectTextAgent) and [`ProjectDataBaseQnA`](https://github.com/Flagro/ProjectDataBaseQnA).

## 🚀 Features

- Specializes in extracting text from various file formats, including Office files.
- Designed to work in both Windows with COM and Linux with LibreOffice + PyUNO. 
- Current implementation supports Linux + LibreOffice + PyUNO.
- Windows support with COM environment is planned for robust file handling.

## 📥 Installation

To install `ProjectText`, use the following pip command:
```bash
pip3 install git+https://github.com/Flagro/ProjectText.git
```


## 🛠️ Usage

Run `ProjectText` from the bin folder with these arguments:

1. `path`: Path to the file or directory to process.
2. `-t` or `--temp`: (Optional) Path to a custom temporary folder.
3. `-p` or `--project`: (Optional) Path to the project folder the file belongs to.
4. `--ignore`: (Optional) Comma-separated list of patterns to ignore.

### 🖥️ Example Command
```bash
projecttext 'path/to/file' --temp 'path/to/temp' --project 'path/to/project' --ignore 'pattern1,pattern2'
```

## 🤝 Contributing

We welcome contributions from everyone. Here's how you can contribute:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.