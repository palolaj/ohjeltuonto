class Project:
    def __init__(self, name, description, licenses, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.licenses = licenses
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return "\n-".join(dependencies) if len(dependencies) > 0 else "\n-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.licenses or '-'}"
            f"\n\nAuthors: {self._stringify_dependencies(self.authors)}"
            f"\n\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
