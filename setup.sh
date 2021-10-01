
# MacOS System

# Show hidden files in finder
defaults write com.apple.finder AppleShowAllFiles YES

# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install brew
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installing all brew packages
brew bundle

stow bash -t $HOME

rm -f $HOME/.zshrc
stow zsh/rc -t $HOME

rm -f $ZSH_CUSTOM/aliases.zsh
stow zsh/aliases -t $ZSH_CUSTOM


rm -f $ZSH_CUSTOM/themes/*
stow zsh/themes -t $ZSH_CUSTOM/themes

stow maven -t $HOME

# git
stow git -t $HOME/
git config --global core.excludesfile $HOME/.gitignore