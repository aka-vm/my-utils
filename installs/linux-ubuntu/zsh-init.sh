#!/bin/bash

# ask password
sudo -v
# zsh
sudo apt-get install zsh
chsh -s $(which zsh)

# oh-my-zsh
sudo apt-get install git curl
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# set  ZSH_THEME="powerlevel10k/powerlevel10k” to .zshrc
# install powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh}/themes/powerlevel10k
echo "Add this ->"
echo "ZSH_THEME=\"powerlevel10k/powerlevel10k\""