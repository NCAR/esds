---
author: Max Grover
date: 2021-5-6
tags: editor, paired-programming, remote-access
---

# Paired Programming using VS Code

A common task when developing notebooks or packages is collaborating with others. It can be challenging to do this when using JupyterHub since two people cannot access the same notebook at same time. One solution to this is to use Visual Studio Code (VS Code) to remotely access Casper/Cheyenne, use a virtual meeting plaform (Zoom, Google Meet), and interactively collaborate on development.

This process includes a few steps:

1. Download VS Code
1. Setup remote login (ssh)
1. Enable sharing
1. Open meeting, share the link
1. Collaborate!

## 1. Download VS Code

Visual studio code is free and openly available. You can find the documentation/download information for your [specific machine here](https://code.visualstudio.com/)

Once you download it, use Self Service to ensure you have the ability to install the software, then open the application once it is installed.

## 2. Setup Remote Login

Once you have VS Code installed, you will need to install the [Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). These extensions are one of the aspects that make this editor so powerful.

Open a terminal in VS Code after installing the extension, and type in the following :

At the top of the VS Code window, select `Remote-SSH: Connect to Host` and enter:

```
user@machine.ucar.edu
```

Replace `user` with your username and `machine` with `casper` or `cheyenne`.

Once you do this once, these settings will be saved, making it easier at a later point to use this login process.

At this point, it will ask you for authentication which is when you will enter your password and follow the dual-authentication.

In the bottom lefthand corner, you will see

```
SSH: machine.ucar.edu
```

which indicates that the remote login as worked!

It will drop you into your home directory, where you can now enter the path you would like to access.

For more details on this process, check out the official [VS Code documentation](https://code.visualstudio.com/docs/remote/ssh)

## 3. Enable Sharing

As mentioned previously, you can share your window interactively with collaborators! The extension that makes this possible is the [Live Share Extension Pack](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack).

Once you install the extension, on the left side of the screen, you will see an arrow icon which is a shortcut to the Live Share tool. Click on that, and connect your Github account. Once you connect your Github account, it will copy the link to you shared session.

At the bottom of the window, you will see your name with a lock next to it. Click on this to find additional sharing options - you can copy the link to the shared session again if you would like.

Additional details about this extension can be [found here](https://code.visualstudio.com/learn/collaboration/live-share)!

## 4. Setup Your Virtual Meeting

Launch your virtual meeting! You can use plaforms such as [Google Meet](https://meet.google.com) or [Zoom](https://zoom.us/)

Once you launch your meeting with collaborators, share the link generated from the previous step (make sure they have followed the same steps, downloading VS Code with all the extensions mentioned).

Within the Live extension pack, there is also an audio option if you prefer not using video services.

## 5. Collaborate!

Once you have everything setup, get to work! You may need to double check the permissions for the sharing extension. Something else that may be helpful is th chat which can be found within the Live Share shortcut on the left side of the screen. Looking at the [documentation for Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack) can be helpful!

I hope this helps you get started using VS Code for paired-programming!
