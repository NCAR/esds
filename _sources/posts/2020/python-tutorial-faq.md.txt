---
author: Julia Kent
date: 2020-10-20
tags: python-tutorial-series,faq,python
---

# Python Tutorial FAQ

Here is a compilation of questions and issues that arose during the first session of the Python Tutorial Seminar Series. Hopefully all attendees feel that their issues are addressed here.

---

**Q.** I am having issues running the command:
`curl -kO https://sundowner.colorado.edu/weather/atoc8/wxobs20170821.txt`.
What should I do?

**A.** If that was your case, try running the above command without the “-kO” option, or try using “wget” instead:
`wget --no-check-certificate https://sundowner.colorado.edu/weather/atoc8/wxobs20170821.txt`.

If you are on Windows and have curl, try:
`curl https://sundowner.colorado.edu/weather/atoc8/wxobs20170821.txt -OutFile wxobs20170821.txt`.

---

**Q.** Can you explain the advantages of each method we just went through?

**A.** In the tutorial part 1 “Opening a .txt File,” we covered 3 different methods of reading in the datafile.
The first used the Python function `readline()` this function only reads a single line from the function and each time you use it, the next line is read. The advantage of this method is that you get to quickly see just the header of the function which is useful for determining how the data is organized.
The second method was to use the Python `read()` function, this reads the entire datafile at once, this is preferred over using method 1 for every single line of the file if you in fact want to read in the entire datafile..
And the third method was the same as the second but using the `with` context manager. The advantage of the third method is that when the with-block is completed the file is automatically closed, making for easier clean up and memory usage throughout the script.

---

Q. When I create the environment, it downloads lots of packages. Are those “python”, or extra things?

A: Yes these are built in packages necessary for Python.

---

**Q.** `git init .` does not work on windows computers. What to do if I neeed to open a git prompt?

**A.** Go inside the YourProject folder, right click and choose Git Bash Here.
On the command line write `git init`

---

**Q.** I had an error at the activate: about initializing my shell, the init command suggested failed as I don't have sudo, what should I do?

**A.** Run `conda init`, Conda will detect the type of shell and write init scripts into the shell’s configuration file. If that doesn't work try `activate env_name` or run from Anaconda command prompt.

---

**Q.** `conda activate python_tutorial` does not work. I get the following error:

```
     CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
     To initialize your shell, run
      $ conda init <SHELL_NAME>
      Currently supported shells are:
      - bash
      - fish
```

What should I do?

**A.** Run `activate env_name` instead of `conda activate env_name`

---

**Q.** `source /Users/hmw/anaconda3/bin/activate` produces the following error:

```
    _CONDA_ROOT=/Users/hmw/anaconda3: Command not found.
    _CONDA_ROOT: Undefined variable.
```

What should I do?

**A.** Run `source activate` instead.

---

**Q.** `git status` produces the following error:

```
        fatal: Not a git repository (or any parent up to mount point /home)
        Stopping at filesystem boundary (GIT_DISCOVERY_ACROSS_FILESYSTEM not set).
```

What should I do?

**A.** You need to run `git init .` before you can run `git status`

---

**Q.** I see the following message:

```
        *** Please tell me who you are.
         Run
         git config --global user.email "you@example.com"
         git config --global user.name "Your Name"

         to set your account's default identity.
         Omit --global to set the identity only in this repository.
```

What should I do?

**A.** This message typically appears the first time you use `git` on a computer. When you make changes in the repository, `git` will track those changes as well as who made them - and to do that, it needs to know your name and email address. Run the two lines mentioned in the error, replacing `you@example.com` with your actual email address and `Your Name` with your name:

```
        git config --global user.email "you@example.com"
        git config --global user.name "Your Name"
```

And then re-run the `git` command that returned the error.

If this is your first time using `git`, we recommend reading the first two chapters of [Pro Git](https://git-scm.com/book/en/v2) to learn more about it. [Chapter 1.6](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) covers this first-time setup step.

---

**Q.** How did you save and exit an editor?

**A.** In vim, it will be `:wq`. In nano it is `Ctrl X`

---

**Q.** Could you explain the logic behind where `()`’s go? We used `datafile = open(filename)` and later `datafile.close()` as opposed to `close(datafile)`. What is the meaning of the `()` after `datafile.close`?

**A.** `open` acts like a built in function in Python. `()` always follow functions. The left hand side `datafile` is defined as a new Python object. Python objects have methods associated with them. One of the functions associated with this object is `close`. So we are accessing the function `close()` from the object `datafile`.

---

**Q.** Are there any good guidelines on when to make something a function vs an object method?

**A.** If you have a collection of functions and those functions all take the mostly same arguments, it is good practice to create an object that holds those shared arguments. We will cover more of this moving forward.

---

**Q.** Can you talk more about how python manages memory when we read data files or create variables within a function?

**A.** Memory management is done through a “garbage collection system” and “instance counting” in Python. The first time you create something in Python, memory is allocated for that thing. Every time you access that variable, it counts how many times there are pointers to that object. Once something is no longer pointed to, Python deletes it from memory.

---

**Q.** In zsh, after running `conda init`, I get an error saying conda is not found...even if I start new zsh shell. What should I do?

**A.** You should be able to get conda to work in zsh directly, if you are comfortable with zsh. It turns out that to do this all you need to do is look inside your "~/.bash_profile" file for a section of code that starts with the line:
`# >>> conda initialize >>>`

and ends with the line:
`# <<< conda initialize <<<`

If you copy these lines and paste them into a file called "~/.zshrc", then conda will work with zsh.

---

**Some other tips for success:**

- For non mac users, git and conda have 2 different shell environment
- You need to use a text editor - for example nano, vim, or nedit. If you are unfamiliar with text editors pick one
- If the commands at the bottom of the screen are hidden by your Zoom toolbar or meeting controls, you need to change the Zoom settings on your display.
- Here is a video about installing miniconda on windows 10: [Install Miniconda and Python 3.7 on Windows 10](https://www.youtube.com/watch?v=tXgPY4lc6fo)
- Here is a video about installing anaconda on windows 10: [Install Anaconda Python, Jupyter Notebook And Spyder on Windows 10](https://www.youtube.com/watch?v=5mDYijMfSzs)
- Here is a video about installing git and configure git and github on windows: [How to Install and Configure Git and GitHub on Windows](https://www.youtube.com/watch?v=J_Clau1bYco)
