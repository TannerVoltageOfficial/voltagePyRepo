import os
import json
import requests
import shutil
from typing import Dict, List

class PackageManager:
    def __init__(self, packages_dir: str = "packages"):
        self.packages_dir = packages_dir
        self.package_info_file = "package_info.json"
        self._ensure_package_dir()
        self._load_package_info()

    def _ensure_package_dir(self):
        if not os.path.exists(self.packages_dir):
            os.makedirs(self.packages_dir)

    def _load_package_info(self):
        if os.path.exists(self.package_info_file):
            with open(self.package_info_file, "r") as f:
                self.package_info = json.load(f)
        else:
            self.package_info = {}

    def _save_package_info(self):
        with open(self.package_info_file, "w") as f:
            json.dump(self.package_info, f, indent=2)

    def install(self, package_name: str, version: str = "latest"):
        print(f"Installing {package_name} ({version})...")
        # In a real implementation, you would download the package from a repository
        # For this example, we'll just create a dummy file
        package_dir = os.path.join(self.packages_dir, package_name)
        os.makedirs(package_dir, exist_ok=True)
        with open(os.path.join(package_dir, f"{package_name}.py"), "w") as f:
            f.write(f"# Dummy file for {package_name}\n")
        
        self.package_info[package_name] = {"version": version}
        self._save_package_info()
        print(f"{package_name} ({version}) installed successfully.")

    def uninstall(self, package_name: str):
        if package_name not in self.package_info:
            print(f"{package_name} is not installed.")
            return

        print(f"Uninstalling {package_name}...")
        package_dir = os.path.join(self.packages_dir, package_name)
        shutil.rmtree(package_dir)
        del self.package_info[package_name]
        self._save_package_info()
        print(f"{package_name} uninstalled successfully.")

    def list_packages(self) -> List[Dict[str, str]]:
        return [{"name": name, "version": info["version"]} for name, info in self.package_info.items()]

    def update(self, package_name: str):
        if package_name not in self.package_info:
            print(f"{package_name} is not installed.")
            return

        print(f"Updating {package_name}...")
        # In a real implementation, you would check for updates and download the latest version
        # For this example, we'll just update the version number
        self.package_info[package_name]["version"] = "latest"
        self._save_package_info()
        print(f"{package_name} updated successfully.")

# Usage example
if __name__ == "__main__":
    pm = PackageManager()

    # Install a package
    pm.install("example_package", "1.0.0")

    # List installed packages
    print("Installed packages:")
    for package in pm.list_packages():
        print(f"{package['name']} - {package['version']}")

    # Update a package
    pm.update("example_package")

    # Uninstall a package
    pm.uninstall("example_package")