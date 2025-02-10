import requests
import json
import os

def get_latest_release_info(repo_url, beta_flag_filepath=None):
    """Retrieves release info, handling beta flag."""

    use_beta = False
    if beta_flag_filepath and os.path.exists(beta_flag_filepath):
        use_beta = True

    if use_beta:
        try:
            commits_url = repo_url.replace("github.com", "api.github.com/repos") + "/commits"
            commits_response = requests.get(commits_url)
            commits_response.raise_for_status()
            latest_commit_sha = commits_response.json()[0]['sha']
            release_info = {'tag_name': latest_commit_sha}  # Fake release info for beta
            print("Using beta version (latest commit).")
            return release_info
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving commit info: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding commit JSON: {e}")
            return None
        except IndexError:
            print("Error: No commits found for beta.")
            return None
    else:
        try:
            api_url = repo_url.replace("github.com", "api.github.com/repos") + "/releases/latest"
            response = requests.get(api_url)
            response.raise_for_status()
            print("Using latest release.")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving release info: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding release JSON: {e}")
            return None


def get_pkgs_json_from_release(release_info, repo_url, beta_flag_filepath=None):
    """Retrieves and parses pkgs.json from a release."""

    use_beta = False
    if beta_flag_filepath and os.path.exists(beta_flag_filepath):
        use_beta = True

    if release_info is None:
        return None

    try:
        if use_beta:
            tag_name = release_info['tag_name'] # Use commit sha as tag name for beta
            pkgs_url = f"https://raw.githubusercontent.com/TannerVoltageOfficial/voltagePyRepo/{tag_name}/pkgs.json" # Correct URL for beta!

        else:
            tag_name = release_info['tag_name']
            pkgs_url = f"https://raw.githubusercontent.com/TannerVoltageOfficial/voltagePyRepo/{tag_name}/pkgs.json" # Correct URL for release!

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
    repo_url = "https://github.com/TannerVoltageOfficial/voltagePyRepo"
    beta_flag_filepath = "beta.flag"  # Path to your beta flag file

    release_info = get_latest_release_info(repo_url, beta_flag_filepath)

    if release_info:
        print("Release Info:")
        print(json.dumps(release_info, indent=4))

        pkgs_data = get_pkgs_json_from_release(release_info, repo_url, beta_flag_filepath)

        if pkgs_data:
            print("\npkgs.json Data:")
            print(json.dumps(pkgs_data, indent=4))

            try:
                print("\nFirst Package:")
                print(pkgs_data[0])
            except IndexError:
                print("Error: pkgs.json does not contain a first element.")
            except KeyError as e:
                print(f"Error: Key '{e}' not found in the first package.")
        else:
            print("Failed to retrieve or parse pkgs.json.")
    else:
        print("Failed to retrieve release information.")

if __name__ == "__main__":
    main()
