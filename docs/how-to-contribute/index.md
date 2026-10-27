---
title: How to Contribute
tags: [Contributing]
---

CAKEbox is hosted on GitHub, making it easy to suggest changes, share useful resources and contribute your own work. If you've found something that could help others, we'd love you to share it!

**There are several ways to contribute, from sharing a quick tip to adding a resource of your own.**


## The easiest way: submit a resource

Have a useful tip, idea or resource to share? You can contribute a Sprinkles of Knowledge quick tip or suggest a link to a resource you've found valuable by completing a short form.

Simply add a title, include your tip or paste a link, and select the relevant themes and keywords to help others discover it.

[Submit or browse resources here.](../all.md)

## I have a resource I'd like to add to CAKEbox

If you'd like to host your resource on CAKEbox, follow the instructions below. The process depends on the format of your resource.

### Option 1: Add a Markdown document

If your resource is written in Markdown:

* Fork the CAKEbox repository and create a new branch.
* Create a Markdown (`.md`) file in the resources directory.
* Add a title to the document using the following format:

    ```bash 
        ---
        title: "Title of your resource"
        ---
    ```

* Add your content and save the file.

### Option 2: Upload a PDF or another file

If your resource is a PDF or another file that can be linked to from a webpage:

* Fork the CAKEbox repository and create a new branch.
* Upload your file to the resources directory.

### Make your resource discoverable

Whichever format you choose, you'll need to add a complementary `.yml` file so that your resource can be found through CAKEbox's themes and keywords.

* Choose the relevant theme directory within `/data`.
* Create a `.yml` file containing the following information:
    ```bash 
    type: resource
    title: "Title of your resource"
    url: "https://www.cake.ac.uk/CAKEbox/resources/name-of-your-resource/"
    comment: "Tell us a little about the resource"
    theme: theme
    keywords:
    - keyword
    - another-keyword
    ```

* Replace the example values with the details of your resource. Choose a clear, descriptive title and relevant keywords to help people find it.
* Commit your changes and submit a pull request (PR) for review.

## Something else? 

Not sure where to start? No problem! Email the committee ([cake@jiscmail.ac.uk](mailto:cake@jiscmail.ac.uk)) and we'll be happy to help you add your resource.

---

## Helpful guides on how to contribute: 

<!-- material/tags {include: [Contributing]} -->
