<!-- [_Stack Overflow: _]() -->
<!-- [_GitHub: _]() -->

# <img src="/imgs/sql.png" width="24" height="24"> SQL

- [_PostgreSQL_](https://www.postgresql.org/docs/)
- [_SQLite_](https://www.sqlite.org/docs.html)

***

# <img src="/imgs/terminal.png" width="24" height="24"> Unix / Linux

- [__Commands__](/terminal/Unix.md)
- [__`vim`__](/terminal/vim.md)
- [__`alias`__](/terminal/alias.md)
    - [_[RU] YouTube: Создание псевдонимов команд (alias)_](https://www.youtube.com/watch?v=HvwOtqEheZ4)
    - [_Stack Overflow: Alias takes a parameter_](https://stackoverflow.com/questions/7131670/make-a-bash-alias-that-takes-a-parameter)
- [__macOS__](/macOS.md)
  - ZSH
  - `brew install tree`
  - iTerm

## Terminal

- [_Oh My Zsh_](https://ohmyz.sh)
  - ```source ~/.bash_profile``` <br> Add to `~/.zshrc`
  - Style:
    - [_powerlevel9k_](https://github.com/Powerlevel9k/powerlevel9k)
    - [_powerlevel10k_](https://github.com/romkatv/powerlevel10k)
    - [_Nerd Fonts_](https://github.com/ryanoasis/nerd-fonts)
    - `DEFAULT_USER=$(whoami)` <br> Remove hostname
    - Style example
        ```sh
        POWERLEVEL9K_MODE='nerdfont-complete'
        # ZSH_THEME="powerlevel9k/powerlevel9k"
        ZSH_THEME=powerlevel10k/powerlevel10k
        DEFAULT_USER=$(whoami)
        ```
  - Plugins:
    - [_zsh-syntax-highlighting_](https://github.com/zsh-users/zsh-syntax-highlighting)
    - [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)  

***

# [macOS](/macOS/README.md)

- App
<!-- - Settings -->

***

# <img src="/imgs/git.png" width="24" height="24"> [`Git`](/git/README.md)

# <img src="/imgs/adb.jpeg" width="24" height="24"> Android Debuging Bridge (adb)

- [__`adb - commands`__](/adb/adb.md)
- [__adb - KeyEvent__](/adb/adb%20-%20KeyEvent.md)

***

# <img src="/imgs/shortcuts.jpeg" width="24" height="24"> IDEs

- [IntelliJ IDEA](/IDEA_shortcuts.md)
- [Visual Studio Code](/VS_Code.md)
- [_PyCharm_](https://www.jetbrains.com/pycharm/)
- [_DataGrip_](https://www.jetbrains.com/datagrip/)
- [_Xcode_](https://itunes.apple.com/us/app/xcode/id497799835)
                    
***

# <img src="/imgs/bootstrap.jpg" width="24" height="24"> Bootstrap

- [__Bootstrap Notes__](/bootstrap_notes.md)
- [_Bootstrap docs_](https://getbootstrap.com/)

***

# <img src="/imgs/study_res.png" width="24" height="24"> Study Resources

[Study resources links](/Study_Resources.md)

*** 

# <img src="/imgs/markdown.png" width="24" height="24"> Markdown

[_Markdown_](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

*** 

# <img src="/imgs/maps.png" width="24" height="24"> Google Maps API

Add Google map place in iframe. `Find place at Google map -> Share -> Embed a map`

- [_Place ID Finder_](https://developers.google.com/maps/documentation/javascript/examples/places-placeid-finder)
- [_Google Map - Hello World_](https://developers.google.com/maps/documentation/javascript/examples/map-simple)

***

# Apache Server

Test config

`apache2ctl configtest`

Set Config

`sudo a2ensite <file>.conf`

`sudo service apache2 restart`

Read log

`sudo tail -100 /var/log/apache2/error.log`

***

# <img src="https://github.com/sergius-la/icon_links/blob/master/img/bash.png" width="28" height="28"> [`Bash`](https://github.com/sergius-la/Cheatsheet/blob/master/bash/README.md)