# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH

#  trying to pull/push commits from/to the Git repository, the bash shell tries to
#  open the gnome-ssh-askpass dialogue and it fails.
#  I wanted to prevent the bash shell from attempting to launch the dialogue box.
unset SSH_ASKPASS
