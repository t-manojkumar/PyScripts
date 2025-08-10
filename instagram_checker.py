import pandas as pd

def find_non_followers(followers_file, following_file):
    """
    Compares followers and following lists to find users who don't follow back.

    Args:
        followers_file (str): The file path for the followers CSV.
        following_file (str): The file path for the following CSV.

    Returns:
        list: A sorted list of usernames that do not follow you back.
    """
    try:
        # Read the CSV files into pandas DataFrames
        followers_df = pd.read_csv(followers_file)
        following_df = pd.read_csv(following_file)

        # Extract the 'username' column and convert to a set for efficient lookup
        followers_usernames = set(followers_df['username'])
        following_usernames = set(following_df['username'])

        # Find the users who you follow but who don't follow you back
        # This is done by finding the difference between the two sets
        not_following_back = following_usernames - followers_usernames

        # Return a sorted list of the usernames
        return sorted(list(not_following_back))

    except FileNotFoundError as e:
        print(f"Error: The file could not be found. Please check the file path.")
        print(f"Details: {e}")
        return None
    except KeyError as e:
        print(f"Error: A 'username' column was not found in one of the files.")
        print(f"Please ensure both files have a column named 'username'.")
        return None


if __name__ == "__main__":
    # Define the names of your files
    followers_filename = '_Followers.xlsx - Sheet1.csv'
    following_filename = '_Following.xlsx - Sheet1.csv'

    # Get the list of users who are not following you back
    non_followers_list = find_non_followers(followers_filename, following_filename)

    # Print the results
    if non_followers_list is not None:
        print("--- Users Who Do Not Follow You Back ---")
        if non_followers_list:
            for username in non_followers_list:
                print(username)
        else:
            print("Congratulations! Everyone you follow also follows you back.")
        print(f"\nTotal users not following back: {len(non_followers_list)}")