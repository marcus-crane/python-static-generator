# utf9k

This README is more just to explain to myself what I'm trying to achieve rather than to explain why you might want to look at/fork this repo.

I've always hacked away at different versions of my site ([https://thingsima.de](https://thingsima.de)) and never been quite happy with the end result. It's a mix of content that is dynamic and static when I wish it was either one or the other.

Blog posts are stored as Markdown, but really I would prefer to have them live as static files. Having said that, something like [Jekyll](https://jekyllrb.com) isn't super appealing to me as the underlying libraries are abstracted away into one single Gem. I'd prefer to have complete control over every element, even though I shouldn't necessarily need to. It's also written in Ruby which is neat but I don't want to have to learn another language just to modify my site.

On the flipside, my [stats](https://thingsima.de/stats) page is completely dynamic, using a [RabbitMQ](https://rabbitmq.com) queue managed with [Celery](https://celeryproject.com) that pulls from various APIs and dumps the results into a [PostgreSQL](https://postgresql.com) instance. It's neat but kinda overkill for what it does.

Ultimately, I want to distil everything into one static site that still has dynamic elements but isn't reliant on them. I basically want to embrace the idea of using Javascript to enhance my site but without it being required if I wanted to view my content using something like [lynx](https://lynx.browser.org).

This whole thing started when I came across [sorg](https://github.com/brandur/sorg) which is the repo that generates [https://brandur.org](https://brandur.org). It's kind of overkill just to serve up some text but something about knowing everything was either handmade or hand chosen for my personal site appeals to my little pea brain, haha.

# Types of content

Here's some links that describe different types of content I want to host on my site. They're all just markdown but with slight variations:

* [articles](/docs/articles.md)
* [projects](/docs/projects.md)
* [reviews](/docs/reviews.md)
* [snippets](/docs/snippets.md)
* [thoughts](/docs/bites.md)
