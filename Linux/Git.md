# Git

Git is a version control tool used to track changes for project files.

TODO:

1. Reserach remotes
    * Git push origin == connecting to remote?
    * What are remotes??
2. Research `git rebase` and `git cherry-pick` with use cases

## Basics

Git tracks file changes and who made them. Before we enable Git, we have to set
who the author for these changes is. Then we enabled Git in a project with the
`git init` command:

```console
$ git config --global user.name "Jerry TheMouse"
$ git config --global user.email "jerry@example.com"
$ cd $PROJECT_DIRECTORY
$ git init

Initialized empty Git repository in $PROJECT_DIRECTORY
```

Git tracks files by attaching changes to _commits_ and adding them to a history
of commits. Git commits contain a lot of information, most notably the author
of the change, their email, the commit message, the files changed, and the hash
which uniquely identifies the commit.

## Workflow

The basic Git workflow is: **Working directory -> Staging Area -> Commit History**

1. **Working directory** - Local folder git is tracking.
1. **Staging Area** - File snapshots that are ready to be committed.
1. **Commit History** - File snapshots that have been committed.

The commands commonly used for this process are:

1. `git status` - shows file changes and fils in the staging area.
1. `git add` - adds files to the staging area
    * `-A/--all/.` - adds all files to staging
1. `git commit` - opens the default editor to write a commit message, then
commits the file changes to the local commit history.
    * `-m $MESSAGE` - specify the message without opening the editor
    * `-am $MESSAGE` - one liner to add, write a message, and commit.

To view the local commit history, you would use:

1. `git show $HASH` -  for a detailed view of the specified commit (most recent
commit if nothing is specified)
1. `git log` - for a detailed view of history
1. `git reflog` - for a more simple view of history

```console
$ git show

Author:  <Jerry@JDESKTOP.localdomain>
Date:   Fri Jun 19 22:51:05 2020 -0500

    added app styles.

diff --git a/styles.css b/styles.css
new file mode 100644
index 0000000..e69de29

$ git log

commit ecba86984cda372c3165a43b6d3234bef321d019
Author:  <Jerry@JDESKTOP.localdomain>
Date:   Fri Jun 19 22:51:05 2020 -0500

    added app styles.

commit 020533053516efa3192cc4a1d25cf2817ffae02b
Author:  <Jerry@JDESKTOP.localdomain>
Date:   Fri Jun 19 22:50:52 2020 -0500

    added site structure.

commit d3dc44ca17c94dbd108afc6c5af4b7c35fb71135
Author:  <Jerry@JDESKTOP.localdomain>
Date:   Fri Jun 19 22:50:24 2020 -0500

    added app logic.

$ git reflog

ecba869 HEAD@{0}: commit: added app styles.
0205330 HEAD@{1}: commit: added site structure.
d3dc44c HEAD@{2}: commit (initial): added app logic.
```

### Branching

Git branches allow us to split up the commit history. This is useful for starting
a new line of development for adding new features or modifying a project without
altering the original. Since all commits are recorded in the history of your
branch, those changes aren't reflected on the main branch. If you do want those
commits to be included in the commit history of the main branch, you would then
perform a _merge_ from the main branch.

Some basic branching commands:

* `git branch $BRANCH` - Creates a branch (shows local branches if $BRANCH isn't
specified)
  * `-m $NEW_NAME` - Renames current branch.
  * `-d $BRANCH` - Deletes a _merged_ local branch.
  * `-D $BRANCH` - Deletes an _unmerged_ local branch.
* `git checkout $BRANCH` - Switches branches.
  * `-b $BRANCH` - Creates a branch and switches to it.
* `git merge $BRANCH` - Merges a branch into the current one.

### Remote

Git repositories can be hosted remotely in services like GitHub, BitBucket, and
GitLab.

> Local working directory/staging area/commit history is copied to the remote
respository and changes in one might not be reflected in the other.

* `git push origin $BRANCH` - Pushes commits to the remote repository.
* `git pull origin $BRANCH` - Pulls commits from the remote repository.
* `git push origin --delete $BRANCH` - Deletes remote branch.

## Advance Use

## Other

### Error Handling

**--amend** - Modifies the most recent commit message.

### .gitignore

### SSH

SSH Keys allow for public/private key encryption when accessing remote repositories.

* Generate SSH keys with `ssh-keygen -b 4096 -t rsa -C "your comment here"`

> Most people use their email for the comment string.
