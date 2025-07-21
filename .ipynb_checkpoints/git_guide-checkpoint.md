# Setup Git

*This guide is compiled from Software Carpentry and Jia Xu's/John (Fritz) Raffensperger's course (Computational Methods for Operations Research and Data Science).*

Git is a widely-used software version control system, initially developed by Linus Torvalds (he also wrote Linux) in 2005. The tag line from the [git website](https://git-scm.com/):

>*Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.*

Git keep track of all of your code (and all of their history). So if you screw up you can always revert the offending changes. Git also manages code merging and parallel development across large teams. Think of it as SharePoint/TeamSpace (except one that actually works). Git is important not only because of its power and utility but also because it is *the* platform for massively distributed open-source software development. The best example of this is [GitHub](https://github.com/trending) - a web platform built on top of Git to allow for collaborative open source development across the world.

Git is a distributed version control system (DVCS) it keeps a full repository of the code in your project folder (in a hidden folder) and syncs the local code with a cloud-based repository, like [RAND Code Exchange](code.rand.org). We will set up both components.

### Install the Local Git Client

To enable local repositories you must install the git client. Grab it from the Git website:

- [Git](https://git-scm.com/downloads)

Another way to install Git is to install the [GitHub client](https://desktop.github.com/), which comes with Git, a graphical front-end and, for the Windows platform, a shell for interacting with Git.

While you are at it, you can also check out the basics of Git and play with the Git intro tutorial.

- [Why Git?](https://git-scm.com/about)
- [Try Git](https://try.github.io/levels/1/challenges/1)

### Setup your RAND Code Exchange Account

We will be hosting our class material on the RAND Code Exchange (Which is based on the open source GitLab web platform). To set up the ability to sync with our RAND Git repository. Follow instructions on the intranet:

- [Instructions for RAND Code Exchange](http://intranet/wiki/index.php/Welcome_to_the_RAND_Code_Exchange)

### Install a Graphical Interface for Git

Git is primarily a command line application. While for many this is the *preferred* approach to use Git, the multitude of commands and advanced features can be overwhelming for novices (it is for me at least). We recommend students start with a graphical front-end for Git. One of the best free, cross-platform options is SourceTree. You can install it here:

- [SourceTree](https://www.sourcetreeapp.com/)

You might be prompted to sign up for an Atlassian account to activate the SourceTree application. This is OK. You will not have to use the account for anything after the fact

Also take a look at the SourceTree tutorial [here](http://rancoud.com/sourcetree-git-use/)


# Using Git


1. Install the [git client](https://git-scm.com/) by itself or as part of the [github](https://desktop.github.com/) package.

2. Before starting, you may have to setup an identity for your git profile:

    ~~~shell
    git config --global user.name "Your name here"
    git config --global user.email "you@rand.org"
    ~~~
