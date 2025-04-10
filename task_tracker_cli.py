import argparse

# list of commands:
# add
# update
# delete
# list | empty means all; available statuses: todo, in-progress, done
# mark-in-progress
# mark-done
def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI - Manage your tasks the easy way")
    parser.add_argument("add", "Add new task")

if __name__ == '__main__':
    main()