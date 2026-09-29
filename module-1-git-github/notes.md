# Module 1 — Git & GitHub

**Student:** Lacanlale, Kyla G.
**Date:** 09/26/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git tracks changes and records your project's history. Since Git saves a history of your changes, you can alway go back to a previous version of your project whenever you make mistakes. Git is also helpful for collaborations. Since it tracks changes, you can check what was changed. It also allows you to work in an isolated workspace where you can work on the project without affecting the main code.

Meanwhile, GitHub is where you can store your projects. It's also a platform where you can share your project with others and collaborate. GitHub makes storing, sharing, and collaboration easier. It eliminates the hassle of sending a file back and forth just to get the latest version.

In short, Git is the tracker, and GitHub is the storage.

---

## Key vocabulary (in your own words)

- repository: the folder in GitHub where thae project is stored and what Git keeps track of.
- commit: saves the changes made to a project in Git's history, which allows developers to easily go back to previous versions.
- branch: an isolated workspace where developer can work on a project without affecting the main branch.
- push / pull: push sends the commited changes to the remote repository, while pull is gets the latest changes from the remote repository to the local copy.
- pull request: a request that asks other collaborators to review the pushed staged changes before merging it to the main project.
- merge conflict: happens when two peope made changes in the same part of the file and pushed the commited changes to the repository

---

## Walking through what I did

After getting the local copy of the repository, I used git checkout to create a branch named module-1 for my commits as I answer this module. I also used git branch just to make sure I am at the right branch. After confirming, I started answering and once I finished, I used git add . to stage all changes I made, then git commit -m with a message of what I did to save the staged changes. After that, I used push -u origin module-1 to push all the saved changes to the remote repository. I then went to the repository in GitHub to create a pull request. Since I am working on this module alone, there were no merge conficts and I am able to merge the changes to the repository. After that, I switched to main branch using git switch and used git pull to pull the updates in the remote repository.

```
git checkout -b <branch name>
git branch
git add .
git commit -m "<message>"
git push -u origin module-1
git switch main
git pull

```

---

## A mistake I made (or one I want to avoid)

A mistake I always make was not saving the the changes I made locally before performng the git add. I alwasys forget that I need to save the changes first locally before staging the changes, so I get confused when I suddenly get an error message telling me that I don't have any changes to stage when I just finished my edits. When that happens, I just check the tab if it has the indication that I haven't saved the file. When I do, I just save it then I proceed to stage, commit, and push the changes.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
