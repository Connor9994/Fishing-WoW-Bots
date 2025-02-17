import os
import subprocess
import random
from datetime import datetime, timedelta

def write_counter(file_path, count):
    # Write the counter to the text file
    with open(file_path, 'w') as f:
        f.write(str(count))

def commit_changes(date, file_path):
    # Set GIT_COMMITTER_DATE for the commit date
    os.environ['GIT_COMMITTER_DATE'] = date.strftime('%Y-%m-%d %H:%M:%S')
    os.environ['GIT_AUTHOR_DATE'] = date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Stage the file
    subprocess.run(['git', 'add', file_path])
    
    # Commit changes
    subprocess.run(['git', 'commit', '-m', 'Increment counter'])

def push_changes():
    # Push changes to remote repository
    subprocess.run(['git', 'push'])

def main():
    # Constants
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    FILE_PATH = 'counter.txt'  # Path to your text file
    START_DATE = datetime(2018, 1, 1)  # Start date for commits
    END_DATE = datetime(2025, 1, 4)    # End date for commits

    current_date = START_DATE
    counter = 1

    while current_date <= END_DATE:

        # Get a random number of commits for the current day (between 1 and 16)
        num_commits = random.randint(2, 16)
        print(f"Committing {num_commits} times on {current_date.strftime('%Y-%m-%d')}")

        for _ in range(num_commits):
            write_counter(FILE_PATH, counter)
            commit_changes(current_date, FILE_PATH)
            print(f"Committed '{counter}' for date: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
            counter += 1

        # Push changes to GitHub after committing for the day
        push_changes()

        # Move to the next day
        current_date += timedelta(days=1)

if __name__ == '__main__':
    main()