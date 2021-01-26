使用iterm2后pycharm中的terminal没有显示venv
- solution
> FILEPATH: /Users/username/.oh-my-zsh/custom/themes/powerlevel9k/powerlevel9k.zsh-theme   
> defined POWERLEVEL9K_LEFT_PROMPT_ELEMENTS || POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(`virtualenv` `acaconda` context dir vcs)  
> 在该属性中添加virtualenv
---