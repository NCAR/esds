---
date: 2020-05-08
tags: templating,jinja2
author: Kevin Paul
---

# Templating isn't just for Web Developers!

Recently, I found myself rambling on in an unprepared attempt to
explain templating to a colleague of mine who had no prior experience
with frontend design. It didn't take me long to realize that my
explanation was convoluted and confusing, not that I stopped talking,
mind you. Attribute that to being unprepared, or sleep deprived (i.e.,
child _still_ not sleeping through the night!), or just a bad teacher.

Regardless, I decided to point them to a tutorial online that
_certainly must exist_, but after a brief Google search (which you
should read as, "I didn't find anything in the first page of search
results!"), all I could find were tutorials for frontend developers.
And if you aren't an HTML expert, or already have experience with
Flask or Django, teaching templating in those contexts can actually
be more confusing than illuminating.

So, as I always do when I find myself struggling with something that
I think should be easy, I ask my wife for advise. I tried to explain
the concept of templating to my wife, who is not a software developer
_at all_. My wife looked at me with this look that said, "What's not
to get?" Then she said, "You mean filling out a form letter
automatically..."

Yes. Exactly. And while my palm was hitting my forehead, it occurred
to me that I should write a templating tutorial for those who really
don't have any prior experience with frontend development and who
might even be scared when they read "less-than-h-t-m-l-greater-than".
Today, we'll learn Jinja2 templating through an example use case where
we want to generate a form letter for a number of different addressees.

## Jinja2

I'll be using Jinja2 for this tutorial. It's extremely popular and
widespread in the Python developer community, and it has very good
documentation... except for the fact that all of their documentation
is almost entirely geared toward frontend designers.

You can install Jinja2 with `pip` or `conda` as follows:

```bash
$ pip install Jinja2
```

or

```bash
$ conda install jinja2
```

That's it. You should now be set up with an environment that
has (at least) python3 and jinja2 installed in it.

## The Use Case

Imagine that you are the attorney for an oil tycoon with $4.5M
held in the Bank of [Freedonia](<https://en.wikipedia.org/wiki/Duck_Soup_(1933_film)>).
With tensions mounting between Freedonia and neighboring Sylvania,
and war looming on the horizon, your client has authorized you to
move these assets to another bank outside of Freedonia. Clearly,
your only course of action is to email as many people for whom
you can find addresses to ask them if they would be willing to
hold the assets in their account for the duration of the conflict.
Obviously, you will need to pay them for their kind services, and
the oil tycoon has agreed to authorize you to gift 20% of the assets
to whomever holds them, as payment for their kindness. You just
need some personal information from them and some bank routine
information. That's all. You have obtained your list of addressees
from a kind person working for the humanitarian WikiLeaks "Foundation,"
and now you must craft an email to send to all of these addressees.

So, there is your entirely believable, totally serious, and extremely
common scenario motivating your need to learn templating.

## The Letter

Fortunately, you already have a "template" for a formal _written_ business
letter sitting around on your hard drive. It looks like this:

```text
[Your Address]

[Date]

[Recipient Name]
[Recipient Title]
[Recipient Company]
[Recipient Address]

[Greeting] [Recipient Name]:

[Letter Body]

[Closing],

[Your Name]
[Your Title]
```

Each element in this "template" that is enclosed in `[]`-brackets is
just a placeholder for some other text. Some of that text is short,
like names, titles, or greeting or closing text. Some of that text
will me multi-line input, such as the letter's body and the addresses.
In Python, all you would want to do is something like string
substitution, for example replacing `[Your Name]` with `Jane Smith`.

This is exactly what "templating" is all about. It is, essentially,
just string substitution...but with a touch more sophistication.

## The Jinja2 Template

So, to start out, we are going to convert this text template into a
Jinja2 template. To do so, the easiest first step would be to just
replace every `[]`-bracketted item with a Jinja2 _expressions_,
which are represented with `{{}}`-brackets:

```jinja
{{ your_address }}

{{ date }}

{{ recipient_name }}
{{ recipient_title }}
{{ recipient_company }}
{{ recipient_address }}

{{ greeting }} {{ recipient_name }}:

{{ letter_body }}

{{ closing }},

{{ your_name }}
{{ your_title }}
```

Also, notice that I have converted the text labels inside the
`[]`-brackets into valid Python variable names. Let's assume
that this new _template file_ is called `letter.j2` (where
the `.j2` means it is a Jinja2 template, but Jinja2 does not
care what extension the file actually has).

We can now "write" this letter using Python variables from a
Python script. First, let's start writing a Python script that
can "render" this Jinja2 template:

```python
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./'))
template = env.get_template('letter.j2')

data = {}

print(template.render(**data))
```

If you were to run this script as it current exists, you would
get a lot of blank lines, and some "floating" punctuation.
Something like this:

```text









 :



,



```

This is because the `data` variable is empty. In other words,
all of those `{{ var_name }}` template variables _never got defined!_
Jinja2 assumes that anything that isn't defined is an empty string.

So, if we were to fill in the `data` dictionary with some data
with keys matching the template variables, we should see something
different.

```python
from datetime import datetime

data = {
    'your_name': "Jane Smith",
    'your_title': "Attorney at Law",
    'your_address': """1234 Somewhere Street
Atown, XY  12345""",
    'date': datetime.now().strftime("%Y %B %d"),
    'recipient_name': "Joe Smith",
    'recipient_title': "Head of Marketing",
    'recipient_company': "Better Stuff, Inc.",
    'recipient_address': """5678 Nowhere Drive
Someberg, YZ  56789""",
    'greeting': 'Dear',
    'closing': 'Sincerely',
}
```

And with that change, the output should now look like:

```text
1234 Somewhere Street
Atown, XY  12345

2020 May 11

Joe Smith
Head of Marketing
Better Stuff, Inc.
5678 Nowhere Drive
Someberg, YZ  56789

Dear Joe Smith:



Sincerely,

Jane Smith
Attorney at Law
```

Does it make sense? Let's explain what's going on here.

In our Python code, we are creating some data (literally `data`)
that we want to hand off to the "template engine" to insert into
the template, itself. The template engine (`jinja2`) searches
through the template document for all occurrences of `{{ key }}`
for each `key` in the `data` dictionary (or each keyward argument
in the `render()` function). And it does simple substition of
the string `{{ key }}` with `data[key]`. Any `{{ key }}`
not found in the `data` dictionary will be replaced with an
empty string, and any `key` in the `data` dictionary _not_ found
in the template document will be ignored.

That's it. That's a _lot_ of what templating is all about.

But not everything.

## Jinja2 Statements

This letter template is nice, but we want to send out _emails_,
not actual postage. You don't have time for snail mail!

So, we _could_ write another template for an email, but for the
sake of edification, let's just modify our existing template
to be _dual purpose_. In particular, some of the template
variables are just not used when writing emails (`your_address`,
`date`, `recipient_name`, `recipient_title`, `recipient_company`,
`recipient_address`). But if we leave these variables undeclared,
then there will be odd whitespace at the top of our email. So,
we will add another template variable for the sole purpose of
specifying if the document we are writing is a letter or an
email. We'll label this variable `is_letter`, and we'll
insert it into our template document with some `if` _statements_,
like so:

```jinja
{% if is_letter %}
{{ your_address }}

{{ date }}

{{ recipient_name }}
{{ recipient_title }}
{{ recipient_company }}
{{ recipient_address }}

{% endif %}
{{ greeting }} {{ recipient_name }}:

{{ letter_body }}

{{ closing }},

{{ your_name }}
{{ your_title }}
```

By default, if we don't specify `is_letter` in the
`data` variable in our Python script, it will default
to an empty string. And in Python, that evaluates
to `False` in a boolean check. So, the top part
of our template will not be displayed if `is_letter`
is `False` or unset. That is, you must explicitly
_set_ `is_letter` or it will assume it is an email.

There are a lot more kinds of _statements_ (`{% %}`-syntax)
you can place in your templates, but this is just a
simple example of what you can do.

Note also that these template variables are all native
Python data types, which means you can declare a template
variable to be a `list`, for example, and index into that
list in the template itself.

## Inheritance

The last thing to explain that is useful with templating
is _inheritance_. If we wanted to print out the same
letter for every recipient, we _could_ just as easily
write the `letter_body` in the Python script, itself.
However, since the `letter_body` could be quite long,
we will put it in _another_ template file. One that
inherits from the original.

To do this, we will first change the `letter_body` from
a template _variable_ to a template _block_ in our
`letter.j2` template file, like so:

```jinja2
{% if is_letter %}
{{ your_address }}

{{ date }}

{{ recipient_name }}
{{ recipient_title }}
{{ recipient_company }}
{{ recipient_address }}

{% endif %}
{{ greeting }} {{ recipient_name }}:

{% block letter_body %}
{% endblock %}

{{ closing }},

{{ your_name }}
{{ your_title }}
```

And then we will write a second template file
(called, for example, `scam.j2`), that looks like this:

```jinja2
{% extends "letter.j2" %}

{% block letter_body %}
(...contents of my letter...)
{% endblock %}
```

Now, change our script to render the `scam.j2`
template instead of the `letter.j2` template and
see what it outputs. You should get something like
this:

```text

Dear Joe Smith:


...contents of my letter...


Sincerely,

Jane Smith
Attorney at Law
```

and if you want to remove those extraneous blank
lines, you might want to set `trim_blocks=True` in
the `Environment` declaration. Then, you should
see something like this:

```text
Dear Joe Smith:

...contents of my letter...

Sincerely,

Jane Smith
Attorney at Law
```

And that's it! Now, you are an expert in templating
with Jinja2! Feel free to attempt your own Spanish
Prisoner con. (**_Not advised!_**)

Well, maybe not an _expert_. There's a lot I didn't
talk about that you can read about in the Jinja2
[documentation](https://jinja.palletsprojects.com/).
Hopefully, though, you can see how something like this
can be _extremely useful_ when generating HTML pages
for a website.
