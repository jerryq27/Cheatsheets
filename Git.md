# Git

## Basic Workflow

The basic Git workflow is: **Working directory -> Staging Area -> Commit History**

1. **Working directory** - Local folder git is tracking.
1. **Staging Area** - File snapshots that are ready to be committed.
1. **Commit History** - File snapshots that have been committed.

* `git status` - Shows status of file changes, and files in the staging area.
* `git add $FILE` - Adds file to the staging area.
  * To add all changed files you can use:
    * **.**
    * **-A**
    * **--all**
* `git commit` - Opens the default editor for writing a commit message, commits the file, and adds it to the local commit history.
  * **-m $MESSAGE** - Writes the message without the editor.
  * **-am $MESSAGE** - Adds and commits files with the message.
  * **--amend** - Modifies the most recent commit message.

## Basic Information

* `git log` - Shows local commit information with timestamps and authors.
  * **reflog** - Shows only commit and messages.
* `git show` - Shows detailed information on the last commit.
  * Can specify a commit for details.

## Basic Branching

Branching is a good way to work on features by splitting the commit tree.

* `git branch` - Shows local branches.
  * **$BRANCH** - Creates a new branch.
  * **-d $BRANCH** - Deletes a merged local branch.
  * **-D $BRANCH** - Deletes an unmerged local branch.
  * **-m $NEW_NAME** - Renames current branch.
* `git checkout $BRANCH` - Switches branches.
  * **-b $BRANCH** - Creates a branch and switches to it.
* `git merge $BRANCH` - Merges a branch into the current one.

## Basic Remote Workflow

Git repositories can be hosted remotely in services like GitHub, BitBucket, and GitLab.
> Local working directory/staging area/commit history is copied to the remote respository and changes in one might not be reflected in the other.

* `git push origin $BRANCH` - Pushes commits to the remote repository.
* `git pull origin $BRANCH` - Pulls commits from the remote repository.
* `git push origin --delete $BRANCH` - Deletes remote branch.

## SSH Keys

SSH Keys allow for public/private key encryption when accessing remote repositories.

* Generate SSH keys with `ssh-keygen -b 4096 -t rsa -C "your comment here"`

> Most people use their email for the comment string.

## Notes

* Git push origin == connecting to remote?
* What are remotes??