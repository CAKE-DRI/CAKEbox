---
title: Template for Contributing a new Central Theme
tags: [Contributing]
# tags: [define theme as a tag here]
---


This page serves as both a guide on how to add a new theme to CAKEbox and a template for the required `index.md` page. CAKEbox is organised around a set of central themes to help structure and navigate resources. If you would like to add a new theme, please:

1. Create a new folder under `docs/` using the title of your theme.
2. Within the new folder, create an `index.md` file as a landing page. This template can be used for the content.
3. Define a new `tag` for the theme and apply it consistently to all resources within the folder.


Now, onto the template: 


## Intro

Provide a short introduction to the theme. 

## What is included? 

Outline the sort of resources/scope of the theme you are capturing. 

## What is not included?

If there are any clear overlaps, sign-post where people can find additional resources. For example: 

- Translating research for broader audiences. See **[Communications and Outreach](../communications-and-outreach/index.md)**. 
- Building and sustaining collaborations, which often strengthen applications. See **[Collaborations and Community Building](../collaboration-and-community-building/index.md)**


## Resources

This section displays resources associated with this theme. Resources can be added in several ways:

### (1) Add tagged Markdown files

Add `.md` files to your theme folder and ensure they include the defined theme tag in their front matter. These will automatically appear using:

<!-- material/tags {include: [defined theme tag here]} -->

### (2) Manually link to internal CAKEbox guides

You can add static links to other resources within CAKEbox. For example:

[Example internal link](index.md)

### (3) Link to external resources

You may also signpost relevant external materials. For example:

[CAKE website](https://www.cake.ac.uk/)