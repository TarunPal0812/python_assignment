from analyzer import FileExtensionAnalyzer


def main() -> None:
    files = [
        "resume.pdf",
        "photo.jpg",
        "report.pdf",
        "data.csv",
        "image.png",
        "notes.txt",
        "file",
        "README",
        "archive.tar.gz",
    ]

    analyzer = FileExtensionAnalyzer(files)
    result = analyzer.analyze_extensions()

    print(result)


if __name__ == "__main__":
    main()

# Output
# {'pdf': 2, 'jpg': 1, 'csv': 1, 'png': 1, 'txt': 1, 'gz': 1}
