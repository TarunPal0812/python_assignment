# 15. File Extension Analyzer 
# Given: 
# files = [ 
# "resume.pdf", 
# "photo.jpg", 
# "report.pdf", 
# "data.csv", 
#     "image.png", 
#     "notes.txt" 
# ] 
# Create functions that return: 
# { 
#     "pdf": 2, 
#     "jpg": 1, 
#     "csv": 1, 
#     "png": 1, 
#     "txt": 1 
# } 
# Handle: 
# file 
# README 
# archive.tar.gz 
# Constraint 
# No filesystem is required. Work only with strings.

def get_extension(filename: str) -> str:
    """
    Extract the file extension from a filename.

    Args:
        filename: Name of the file.

    Returns:
        The file extension without the dot.
        Returns an empty string if no extension exists.

    Examples:
        "resume.pdf" -> "pdf"
        "archive.tar.gz" -> "gz"
        "README" -> ""
        "file" -> ""
    """
    if "." not in filename or filename.endswith("."):
        return ""

    return filename.rsplit(".", 1)[1].lower()


def analyze_extensions(files: list[str]) -> dict[str, int]:
    """
    Count the occurrences of each file extension.

    Args:
        files: List of filenames.

    Returns:
        Dictionary containing extension counts.
        Files without an extension are ignored.
    """
    extension_counts: dict[str, int] = {}

    for filename in files:
        extension = get_extension(filename)

        if extension:
            extension_counts[extension] = extension_counts.get(extension, 0) + 1

    return extension_counts


def main() -> None:
    """Run the file extension analyzer."""

    files: list[str] = [
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

    result: dict[str, int] = analyze_extensions(files)

    print(result)


if __name__ == "__main__":
    main()


# Output
# {'pdf': 2, 'jpg': 1, 'csv': 1, 'png': 1, 'txt': 1, 'gz': 1}

