# ZSH_conda
Some random ZSH things which work nicely with anaconda

After install oh_my_zsh I wanted the shell to work better with conda, so here are some bits of code (which are mostly slighlty modified bits of others code) which add some of that integration.

The file append_to_zshrc included two functions to add to your ~/.zshrc file. If you also add the file \_cactivate.sh to a folder (which you may have to make) ~/.oh_my_zsh/completions (or any of the folders in $fpath) then the function cactivate will autocomplete your conda virtual enviroments. If auto complete does not work I suggest you check the path in the file \_cactivate.sh (in the function get_envs()), make sure that is set to where your anaconda installation is.

The file rkj-conda.zsh-theme is an oh_my_zsh theme which added an indicator as to the conda enviroment you are working in to the prompt. 

I've no idea if these will work on others computers, you may have to modify them; however, they work on mine so hopefully they work on yours. 
