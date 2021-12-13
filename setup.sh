
# MacOS System

# Show hidden files in finder
defaults write com.apple.finder AppleShowAllFiles YES

# Install oh-my-zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install brew
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installing all brew packages
brew bundle


.all_stows.sh

# git
stow git -t $HOME/
git config --global core.excludesfile $HOME/.gitignore