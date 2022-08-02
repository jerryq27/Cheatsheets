# Git

Git is a version control tool used to track changes for project files.

TODO:

1. Research `git rebase` and `git cherry-pick` with use cases

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

1. **Working directory** - local folder git is tracking.
1. **Staging Area** - file snapshots that are ready to be committed.
1. **Commit History** - file snapshots that have been committed.

The commands commonly used for this process are:

1. `git status` - shows file changes and fils in the staging area.
1. `git add` - adds files to the staging area.
    * `-A/--all/.` - adds all files to staging.
1. `git commit` - opens the default editor to write a commit message, then
commits the file changes to the local commit history.
    * `-m $MESSAGE` - specify the message without opening the editor.
    * `-m $MESSAGE -m $DESCRIPTION` - specify the message and a longer description.
    * `-am $MESSAGE` - one liner to add, write a message, and commit. Only works for files already being tracked by git.

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
  * `-m $NEW_NAME` - renames current branch.
  * `-d $BRANCH` - deletes a _merged_ local branch.
  * `-D $BRANCH` - deletes an _unmerged_ local branch.
* `git push -d $REMOTE $BRANCH` - deletes a remote branch.
* `git checkout $BRANCH` - switches branches.
  * `-b $BRANCH` - creates a branch and switches to it.
* `git merge $BRANCH` - merges a branch into the current one.

### Remote

Git repositories can be hosted remotely in services like GitHub, BitBucket, and
GitLab.

> Local working directory/staging area/commit history is copied to the remote
respository and changes in one might not be reflected in the other.

* `git remote add $REMOTE` - saves remote location under a name, "origin" is used by default on GitHub.
* `git push $REMOTE $BRANCH` - pushes commits to the remote repository.
* `git pull $REMOTE $BRANCH` - pulls commits from the remote repository.
* `git push $REMOTE --delete $BRANCH` - deletes remote branch.

#### Upstream

Setting the upstream turns a local branch into a _tracking branch_. In other words, it connects
a local branch to a remote branch. Having this set removes the need to specify where to send
commits whenever `git push` is ran.

```console
$ git push origin master # Has to specify remote and branch every time.

$ git push -u origin master # Sets upstream by connecting the current branch to the "master" branch from "origin"
Branch 'master' set up to track remote branch 'master' from 'origin'.

$ git push # Since the upstream is set for the current branch, this will always push to the "master" branch from "origin".
```

## Advance Use

### Reverting Changes

There are a few ways to go back to a previous commit. Some ways involve rewriting
history (dangerous), and others preserve history (recommended).

#### Dangerous Method

This method isn't recommended if you're working with others, since it rewrites history
and other people might have those commits.

`git reset`

* `--soft` - uncommits changes, but leaves them in the staging area.
* `--mixed` - uncommits changes and removes them from the staging area (Default).
* `--hard` - uncommits changes, removes them from the staging area, and deletes them from the working tree.

Uses:

1. `git reset` - removes all files from staging (or certain files if specified).
1. `git reset HEAD~1` - uncommits and unstages files from last commit. A hash can also be specified and all changes after
the has will be uncommited and unstaged.

#### Recommended Method

This method is recommended since it doesn't rewrite history, instead it reverts you files to the specified
commit and then you can commit those reverted changes.

`git revert --no-commit $HASH..HEAD`

> if `--no-commit` isn't specified, you'll be prompted for a message for every commit in the range.

## Other

### Error Handling

`git commit --amend` - Modifies the most recent commit message.
`git add $FILE && git commit --amend --no-edit` - Adds file to previous commit.

### .gitignore

### Tags

Git tags are bookmarks to branches of development. They are usually used to make versions
Since they mark a commit as the fixed state of the project for that tag.

Git supports two types of tags _lightweight_ and _annotated_. Lightweight tags are just

1. Lightweight - just a pointer to a specific commit.
1. Annotated - full object with more information (checksum, tagger name, email, date, and a message)

* `git tag` - list the tags.
* `git show $TAG` - shows the information stored with a tag.
* `git tag $TAG` - creates a lightweight tag.
* `git tag -a $TAG -m $MSG $HASH` - creates an annotated tag with a message at a certain commit (if hash is specified).
* `git tag -d $TAG` - deletes a tag locally.
* `git push origin --delete $TAG` - deletes a tag from a remote repository.
* `git push origin $TAG` - pushes the tag to a remote repositiory.
* `git push origin --tags` - pushes all local tags to a remote repository.

#### Recreate Tag

Steps to recreate a tag that has been pushed to a remote repository:

```sh
git tag -d <tagname>                  # delete the old tag locally
git push origin :refs/tags/<tagname>  # delete the old tag remotely
git tag <tagname> <commitId>          # make a new tag locally
git push origin <tagname>             # push the new local tag to the remote
```

### SSH

SSH Keys allow for public/private key encryption when accessing remote repositories.

* Generate SSH keys with `ssh-keygen -b 4096 -t rsa -C "your comment here"`

> Most people use their email for the comment string.
