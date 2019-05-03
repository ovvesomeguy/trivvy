<p align="center"> 
    <span><img src='icons/logo.png'></img></span>
</p>

# Trivvy is a cool tool to save your time?
Trivvy is project which helping you with creating your own projects using templates.

# INSTALLATION
To install just run this command in your terminal
>sudo ./build.sh
# USAGE
To make the project, run this comand
> trivvy start

If settings.json does not exists, this comand will create him with basic content
```javascript
{
    "path":".",
    "name": "your_folder_name",
    "template": ""
}
```
You need to change "template" property. Two templates are aviable just now:
* python
* web

# List of properties in json file
| Option | Description | Development Status | Status|
|:------:|:-----------:|:------------------:|:-----:|
|**path**|*If "." than create project in this folder* | <span style="color:green">Alpha<span> | Required |
|**name**|*Just name*| <span style="color:green">Alpha<span>| Required|  
|**template**| *Let trivvy know, which template he need to use* | <span style="color:green">Alpha<span> | Required |
|**author**| *This propery use to add project in database* | <span style="color:green">Alpha<span> | Not required |   
|**integrate**| *This is beta function. Now you can use it to create the database in home folder with all of your projects* | <span style="color:orange">Beta<span> | Not required. |
|**github**:|  *Beta - dont work.*  | <span style="color:red">Gamma?<span> | Not required.|

# The templates which you can use right now
Python template have this structure:
```bash
src/
    __init__.py
    __main__.py
settings.json
README.md
```

Web template have this structure:
```bash
images/
src/
    index.html
    style.css
    script.js
settings.json
README.md
```

# Contributors
* **Main developer** - [Really Cool Guy](https://github.com/parsifloor)

# What next?
In the near future, function to adding custom templates will be added.
Some cool featured will be added.
And some very cool, and awesome featured will be added.

# Contacts
* ![github](icons/github.png) [Github](https://github.com/parsifloor)
* ![vl](icons/vk.png) [Vkontakte](https://vk.com/id263838377)
* ![twitter](icons/twitter.png) [Twitter](https://twitter.com/hQECDuaUbjVQGKa?s=09)