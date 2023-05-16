# Common Linux Install Instructions

## update and upgrade

```sh
sudo apt-get update
sudo apt-get upgrade
```

## Install zsh

```sh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/aka-vm/my-utils/master/installs/linux-ubuntu/zsh-init.sh)"
```
## Homebrew

```sh
sudo apt-get install build-essential procps curl file git
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
```

## pyenv
```sh
sudo sh -c "$(curl -fsSL https://raw.githubusercontent.com/aka-vm/my-utils/master/installs/linux-ubuntu/pyenv.sh)"
```