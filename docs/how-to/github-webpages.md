# Very high level to alter something on a github.io webpage

This guide provides some very high-level instructions of how to make changes to github.io webpages using only the browser.
The CAKEbox is using this technology, but also [CAKE itself](https://cake.ac.uk) or [SHAREing](https://shareing-dri.github.io/).
Most people will prefer to use git access directly, but sometimes a quick change through the web is what you want.


## First time

- Create an account at github.com
- Log into github
- At the left, type in your repository name into the **Find a repository...** field. This has to be the github.io URL. If you want to alter CAKE for example, you have to type in cake-dri.github.io, i.e., the URL without the leading https::
- From hereon, this repository should always show up on the left every time you log in

## Edit a file

- Pick the file you want to alter
- Click on the pen the right top which says "Edit"
- Make your changes
- If this is the first time you alter something, it will ask if you want to create a branch or fork. This is your private copy

All your changes will end up in your branch/fork. They will not (yet) be on the webpage, so you can play around with your changes. Everytime you make a change and you are happy with it, klick on Commit changes ... to submit the changes to your local copy.

## Upload changes to the website

To get your changes onto the actual website, you need to issue a pull request, i.e. tell the owner of the website to accept your changes.
For this,

- Click on Pull requests at the very top of the page.
- Pick New pull request.
- Select the webpage's main as base
- Pick your own copy instead of compare:main
- Pick Create pull request
- Feel free to give it a title and confirm your request by clicking on Create pull request once again


