### Default .bashrc Setup
### From J. Farran(original), modified by itoufiqu for HPC3

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

. /data/utils/system-files/system-wide-env-setup/system-wide-bashrc

#ulimit -l unlimited
alias m=less

#umask 027
#umask 022

#PS1='[\u@\h \W]$ '
#PS1='[\u@\h \W]$ '
if [ $(id -u) -eq 0 ];
then # you are root, set red colour prompt
  PS1="\\[$(tput setaf 1)\\]\\u@\\h:\\w #\\[$(tput sgr0)\\]"
else # normal
  PS1="[\\u@\\h:\\w] $"
fi
export VISUAL=vi
export EDITOR=emacs
