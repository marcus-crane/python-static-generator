# Projects

Projects might be a tricky one.

As you can guess by the name, it would be a markdown representation of a project that I've worked on but I'd like to have them differentiated enough.

I think the way to go about this might be support for custom CSS and Javascript. What I could do then is just automatically have the bundler pull in any CSS and JS files with the same name as the project post rather than having to specify them.

Assuming these are primarily programming projects, perhaps some support for pulling information from the Github API and styling to suit the project itself.

It doesn't make much sense to put an exact date on a project so probably just a year would suffice.

I'd also be making use of screenshot/image embedded to illustrate the purpose of each project.

Tagging a project with the different types of languages and/or frameworks might be a neat stretch feature a la platform logos for videogame reviews.

## Metadata

The content block for a project would look a little like this:

```
---
type: project
title: My cool Python project
description: This project does this and that. Whoa!
year: 1970
lang: python
css: /css/my-cool-python-project.css
js: /js/my-cool-python-project.js
---

Here is my neato project. I've written some stuff about it.
```
