import requests
import json

def get_latest_release_info(repo_url):
    """Retrieves information about the latest release from a GitHub repository."""
    api_url = repo_url.replace("github.com", "api.github.com/repos") + "/releases/latest"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving release info: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding release JSON: {e}")
        return None

def get_pkgs_json_from_release(release_info):
    """Retrieves and parses pkgs.json from a release."""
    if release_info is None:
        return None

    try:
        tag_name = release_info['tag_name']
        pkgs_url = f"https://raw.githubusercontent.com/TannerVoltageOfficial/voltagePyRepo/{tag_name}/pkgs.json"
        response = requests.get(pkgs_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving pkgs.json: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding pkgs.json: {e}")
        return None
    except KeyError as e:
        print(f"Error: Key '{e}' not found in release info.")
        return None


def main():
    repo_url = "https://github.com/TannerVoltageOfficial/voltagePyRepo"  # Replace with your repo URL

    release_info = get_latest_release_info(repo_url)

    if release_info:
        print("Latest Release Info:")
        print(json.dumps(release_info, indent=4))  # Print release info nicely formatted

        pkgs_data = get_pkgs_json_from_release(release_info)

        if pkgs_data:
            print("\npkgs.json Data:")
            print(json.dumps(pkgs_data, indent=4)) # Print pkgs.json data nicely formatted

            try:
                print("\nFirst Package:")
                print(pkgs_data)  # Access and print the first package
            except IndexError:
                print("Error: pkgs.json does not contain a first element.")
            except KeyError as e:
                print(f"Error: Key '{e}' not found in the first package.")

        else:
            print("Failed to retrieve or parse pkgs.json.")

    else:
        print("Failed to retrieve latest release information.")

if __name__ == "__main__":
    main()

