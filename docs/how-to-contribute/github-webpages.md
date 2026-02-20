---
title: Editing a GitHub Pages Webpage via Web Browser
tags: [Contributing]
---

# High-Level Guide: Making Small Changes to a GitHub Pages Website

This guide provides some very high-level instructions of how to make changes to github.io webpages using only the browser.
The CAKEbox is using this technology, but also [CAKE itself](https://cake.ac.uk) or [SHAREing](https://shareing-dri.github.io/).

Most people will prefer to use git access directly, but sometimes a quick change through the web is what you want.


## First Time Setup

1. Create a [GitHub account](https://github.com).  
2. Log in to GitHub.  
3. In the **Find a repository…** field (top left), type the repository name (for GitHub Pages, this is the URL without `https://`, e.g., `cake-dri.github.io`).  
4. This repository will now appear on your left sidebar whenever you log in.


## Editing a File

1. Select the repository/project you want to edit.  
2. Navigate to the file you want to change.  
3. Click the **pen icon** in the top right (“Edit this file”).  
4. Make your changes in the browser editor.  
5. If prompted, create a new branch or fork. Give it a meaningful name — this is where your changes will live.  
6. Click **Commit changes** to save them to your branch/fork. These changes will **not yet appear on the live website**.  

You can experiment freely; every commit updates your branch/fork. When ready, you can submit your changes to the main site.


## Publishing Changes to the Website

To update the live site, create a **pull request**:

1. Click **Pull requests** at the top of the repository page.  
2. Select **New pull request**.  
3. Set the repository's `main` branch as the base.  
4. Select your branch/fork for the comparison.  
5. Click **Create pull request**.  
6. Give your pull request a clear title and click **Create pull request** again to submit it.  

The repository owner can now review and merge your changes to the live site.

## Further reading

Most pages on github.io use Markdown syntax - although you can also use HTML. 
A good resource to learn more about Markdown is https://www.markdownguide.org/getting-started.
