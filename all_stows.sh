#!/bin/bash  

stow bash -t $HOME

rm -f $HOME/.zshrc
(cd zsh && stow rc -t $HOME)

rm -f $ZSH_CUSTOM/aliases.zsh
(cd zsh && stow aliases -t $ZSH/custom)

rm -f $ZSH_CUSTOM/themes/*
(cd zsh && stow themes -t $ZSH/custom/themes)


# TODO: fix the .m2 settings file
# stow maven -t $HOME