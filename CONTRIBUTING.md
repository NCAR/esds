# ESDS Blog Contributors Guide

> **Note**: Steps 1-5 are only necessary the first time; once you have forked and cloned the repo you can start at step 6 to create new branches for new contributions

1. From web, fork the ESDS repo
    * “Fork” button in upper right

2. From terminal, navigate to where you’d like to clone the repo

3. Clone your fork
```
git clone git@github.com:$USER/esds.git
```

5. Navigate to cloned repo
```
cd esds
```

6. Add upstream to original repo and verify
```
git remote add upstream git@github.com:NCAR/esds.git
git remote -vv
```

6. Create branch for new blog post and switch to it
```
git checkout -b $BRANCH
git branch -va
```

7. Set tracking information for the branch
```
git branch --set-upstream-to=origin/$BRANCH $BRANCH
```

9. Add and edit file(s) in the appropriate blog post folder, e.g., /posts/2023/  
    * Tip: look at other posts (.md or .ipynb files) to get ideas on formatting
    * To add author/date/tags to a notebook post, click on the settings icon in the top right corner of jupyterlab for the first cell of the notebook (use an existing notebook post to see formatting).

10. When ready, add your changes
```
git add $FILES
```

12. Commit your changes
```
git commit -m "$MESSAGE"
```

13. Push your changes to your fork
```
git push origin $BRANCH
```

15. From web, open a pull request from your fork or the main ESDS repo
    * Github should prompt you to do this with a yellow bar at the top of the screen
    * Add a title and description to the PR
    * You can add/edit reviewers using the panel in the top right of the PR

16. The PR may change text/code via auto-fixes from pre-commit hooks that have been set up in the repository. Be sure to pull these changes to your local clone/branch before making additional changes (e.g., as a result of the PR reviews) or you may end up with merge conflicts.
```
git pull
```

