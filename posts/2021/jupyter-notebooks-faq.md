---
author: Julia Kent
date: 2021-03-03
tags: python-tutorial-series,faq,jupyter
---

# Jupyter Notebooks Tutorial FAQ

Here is a compilation of questions and issues that arose during the [Jupyter Notebooks](https://youtu.be/xSzXvwzFsDU) session of the Python Tutorial Seminar Series.

---

**Q.** I installed Miniconda but it doesn’t seem to be working. `conda` is not a recognized command. What should I do?

**A.** This is possible if Miniconda is not visible from your workspace, according to the [Conda trouble shooting site](https://docs.anaconda.com/anaconda/user-guide/troubleshooting/#cannot-get-conda-to-run-after-installing) this happens if you answered “NO” instead of “YES” when asked if you’d like to prepend the conda prompt to your path. You have two options:

1. Manually edit your (hidden) `.baschrc` file to include the line:

   ```
   export PATH=/Users/your-username/anaconda3/bin:$PATH

   ```

2. Try uninstalling and re-installing Conda, making sure to answer “YES” this time,

---

**Q.** I executed `jupyter lab` and received the message, “Could not determine jupyterlab build status without nodejs”. Do I need to exit somehow and or fix something?

**A.** This is only a warning, not an error message. No fix is necessary.

---

**Q.** How do you specify what browser Jupyter opens with?

**A.** If you don’t want to use your default browser (which Jupyter will automatically open), you can specify a different one with `jupyter lab —browser=chrome` (e.g., for Chrome)

---

**Q.** Jupyter opens to my base environment, not the environment I launched `jupyter lab` from. Is this an error?

**A.** This is the expected behavior. You can double check your environment by typing `conda env list` from your Jupyter terminal to see all of your environments. The one with the asterisks next to it is your activated environment.

---

**Q.** The Jupyter workspace autocompletion of quotation marks and parenthesis is causing errors. Is there a way to disable this?

**A.** Yes according to this this [stack overflow post](https://stackoverflow.com/questions/44216326/how-to-disable-auto-quotes-and-auto-brackets-in-jupyter-5-0#:~:text=2%20Answers&text=After%20executing%20the%20Python%20command,auto%2Dclosing%20quotes%20and%20brackets), in any code cell type:

```
from notebook.services.config import ConfigManager
c = ConfigManager()
c.update('notebook', {"CodeCell": {"cm_config": {"autoCloseBrackets": False}}})
```

You may have to restart the Jupyter session for the changes to take effect.

---

**Q.** Is converting a cell from code to raw a good way to basically “comment out” an entire cell? Is that good practice or bad practice?

**A.** This is the easiest way to "comment out" a cell.

---

**Q.** How do I use Jupyter with an R kernel (instead of Python)?

**A.** You would need to create a new Conda environment with R and `jupyter` installed.

---

**Q.** Does Jupyter Lab care about being shut down gracefully? If I you just `ctrl-C` it from the command-line, does that do anything bad?

**A.** As long as your notebook is saved, `ctrl-C` is fine. Otherwise, you will lose the contents of your notebooks that weren’t saved before the shutdown.

On a Mac you can double check that your Jupyter Notebook isn't still running in the background, type `jupyter notebook list` in the terminal to list all active sessions.

---

**Q.** How do different environments affect resource usage in virtual environments?

**A.** Running code uses resources, different environments use disc space. It is possible to have a ton of duplication (e.g., every single user of the virtual environment has installed `numpy`) but this gives you a lot of control over your own software versioning. You can prune unused virtual environments to save disc space with the command `conda env remove —name my_env`, or try `conda clean -a` to clean up any cached downloaded packages.

---

**Q.** Where are the packages physically installed in a virtual environment?

**A.** In the directory where miniconda was installed, you will see a directory called `envs`, and every single named environment will be put into that directory.

---

**Q.** Why do we install Miniconda instead of Anaconda?

**A.** Miniconda is much more lightweight than Anaconda. It contains fewer packages and takes up less disc space.

---
