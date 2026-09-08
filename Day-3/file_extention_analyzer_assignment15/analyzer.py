class FileExtensionAnalyzer:
    """
    Object-Oriented Analyzer for extracting and counting file extensions from a list of filenames.
    """

    def __init__(self, filenames: list[str]) -> None:
        self.filenames: list[str] = filenames

    @staticmethod
    def get_extension(filename: str) -> str:
        """
        Extract lowercased extension string from filename.
        Returns empty string if no extension is present.
        """
        if "." not in filename or filename.endswith("."):
            return ""
        return filename.rsplit(".", 1)[1].lower()

    def analyze_extensions(self) -> dict[str, int]:
        """Compute frequency breakdown of file extensions."""
        extension_counts: dict[str, int] = {}
        for filename in self.filenames:
            ext = self.get_extension(filename)
            if ext:
                extension_counts[ext] = extension_counts.get(ext, 0) + 1
        return extension_counts
