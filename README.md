# ZSH_conda
Some random ZSH things which work nicely with anaconda

Hello people of the internet! After install oh_my_zsh I wanted the shell to work better with conda, so here are some bits of code (which are mostly slighlty modified bits of others code) which add some of that integration.

## Conda Eviroment Integration
The file append_to_zshrc included two functions to add to your ~/.zshrc file. If you also add the file \_cactivate.sh to a folder (which you may have to make) ~/.oh_my_zsh/completions (or any of the folders in $fpath) then the function cactivate will autocomplete your conda virtual enviroments. If auto complete does not work I suggest you check the path in the file \_cactivate.sh (in the function get_envs()), make sure that is set to where your anaconda installation is.

The file rkj-conda.zsh-theme is an oh_my_zsh theme which added an indicator as to the conda enviroment you are working in to the prompt. 

I've no idea if these will work on others computers, you may have to modify them; however, they work on mine so hopefully they work on yours. 

The files "running_labs", "jlab_start", and "clabstop" should all be added to your PATH for this stuff to have any chance of working for you.

Your prompt should look something like this if the theme was installed correctly:
![alt text](https://github.com/tboudreaux/ZSH_conda/blob/master/Screen%20Shot%202018-07-09%20at%2010.09.57%20AM.png)

where mine says "general" your may say root, or whatever conda enviroment you have sourced. The enviroment name will color green if it a python 3 enviroment and orange if it is a python 2 enviroment. 

You may have to run this command to prevent the enviroment name showing up twice

```bash
conda config --set changeps1 False
```

If you want to use these you will have to go through all the files and make sure that any paths in the files are pointing to valid locations, right now they all either point to valid paths on *my* computer or they have some placeholder text for you to put your desired path in.

## Jupyter "Integration"
Along with showing currently source conda enviroment in the shell I have included some files which make my life easier usign jupyter lab (note I wrote these for jupyter lab, but you could easily modify them to work with jupyter notebook, all you have to do is change the command in jlab_start). Their are 3 main parts: starting labs, stoping labs, and checking which labs are running. by including jlab_start and running_labs in your path, and by including the clab function (in append_to_zshrc) in your .zshrc file and by adding the \_clab.sh to your completions when you type

```bash
clab <tab> 
```

it will autocomplete the avalible enviroments. If you select an enviroment without jupyter lab, or one in which a jupyter lab is already running it will safely terminate. You can also just type ```clab``` and a jupyter lab will run in whatever enviroment you are currently sourced in. You can find which labs are running by typing running_labs (assuming it is in your path), and if for some reason the shell where the lab was started in gets closed and you want to kill the lab you can type clabstop (again assuming its in your path), it will autocomplete the enviroments which have labs running. clabstop will only work properly if *one* lab is running in an enviroment.
