# Drift

Drift 0.0.5 supports Django 1.7 migrations.

Make pages and models easily editable directly by users.

Using an approach similar to the Django admin and using some new style content editable approach to make a better user experience.

More docs, source and examples coming soon.

## History

### 0.0.6

* Modifying `contrib.versionedpages` to prevent deletion on content when
  users are deleted using `on_delete=models.SET_NULL`.

### 0.0.5

* Breaking change, `content.get_form` now requires request be passed in
  as the first argument. Where you have `content.get_form(request.POST)`
  make it `content.get_form(request, request.POST)`. This make translation
  using django-hvad possible.

# Tutorial: Creating a Custom Content Type

Generally a content type will live in its own app which contains the models which back the content type, the content class which is used in the views to control how the type is managed.

## Model

Start with a pretty simple model.

```
#python
    class Foo(models.Model):
        name = models.CharField(max_length=256)
        slug = models.SlugField()
        description = models.TextField()

        published = models.BooleanField(default=True)

        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)

        @models.permalink
            def get_absolute_url(self):
                return ('foo', [self.slug])

        def __unicode__(self):
            return self.name
```

This simple Foo model has a title and description. Generally in the CMS you will want to link to the instances of Foo so having both a `slug` and a `get_absolute_url` is highly recommended.

## Urls and Admin

Next update urls.py to allow our `get_absolute_url` function to kind of work. We will need views before they can.

```
#!python

from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.foos, name="foo_list"),
    url(r'^\+new/$', edit_foo, name="edit_foo"),
    url(r'^(.+)/edit/$', edit_foo, name="edit_foo"),
    url(r'^(.*)/$', foo, name="foo"),
)
```

We also need register the model in the admin, by default drift provides an admin link to edit the item in the admin if that is what is preferred.

```
#python
from django.contrib import admin

from .models import Foo

admin.site.register(Foo)
```

## Content

Before we write the critical views.py and template, let's take a moment to implement the special content.py and object which makes editing the content type through the interface possible. This should feel pretty similar to the admin.

```
#!python
from django.core.urlresolvers import reverse_lazy

from drift import content

from .models import Foo

class FooContent(content.ModelContent):
    name = "Foo"
    contenteditable = ('name', 'description')
    exclude = ('published',)
    prepopulated_fields = {'slug': 'name'}

    def get_new_url(self):
        return reverse_lazy('new_foo')

    def get_edit_url(self):
        if self.instance is not None:
            return reverse_lazy('edit_foo', args=[self.instance.slug])
        return None

content.system.register(Foo, FooContent)
```

`contenteditable` means the field can be edited inline using some special widgets provided by drift. If it isn't listed as `contenteditable` than it appear in the "Content Settings" section of the editing page.

## Views

Finally views and templates need to be created. We need 3 views, viewing a foo, editing a foo and publishing a foo.

```
#python
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from drift.content import make_content

from .models import Foo


def foos(request, template="foo_list.html"):
    foos = Foo.objects.filter(published=True)
    return render(
        request,
        template,
        dict(
            content=make_content(Foo),
            foos=foos,
        ),
    )


def foo(request, slug, template="foo.html"):
    foo = get_object_or_404(Foo, slug=slug)

    return render(
        request,
        template,
        dict(
            content=make_content(foo),
        ),
    )


@login_required
def edit_foo(request, slug=None, template="edit_foo.html"):
    if slug is None:
        foo = Foo()
        create = True
    else:
        foo = get_object_or_404(Foo, slug=slug)
        create = False

    content = make_content(foo, request, 'create' if create else 'edit')

    if request.method == "POST":
        form = content.get_form(request, request.POST)
        if form.is_valid():
            foo = form.save()
            return redirect('foo', foo.slug)

    return render(
        request,
        template,
        dict(
            edit=True,
            content=content,
        ),
    )

```

## Templates

Define your foo_list.html, foo.html and edit_foo.html templates and you should be ready to test.

```
#html
{% extends 'base.html' %}

{% block head_css %}
        {{ block.super }}
        {% if user.is_staff %}
        <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}css/content.css"/>
        {% endif %}
{% endblock head_css %}

{% block head_js %}
        {{ block.super }}

        {% if user.is_staff %}
        <script type="text/javascript" src="{{ STATIC_URL }}js/csrf.js"></script>
        <script type="text/javascript" src="{{ STATIC_URL }}js/content.js"></script>
        {% endif %}
{% endblock head_js %}

{% block contents %}
{% include 'content/control_panel.html' %}
    <h1>Foos</h1>
    {% for foo in foos %}
    <p>
    <a href="{{ foo.get_absolute_url }}">{{ foo.name }}</a>
    </p>
    {% endfor %}
{% endblock contents %}
```

```
#html
{% extends 'base.html' %}

{% block head_css %}
        {{ block.super }}
        {% if user.is_staff %}
        <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}css/content.css"/>
        {% endif %}
{% endblock head_css %}

{% block head_js %}
        {{ block.super }}

        {% if user.is_staff %}
        <script type="text/javascript" src="{{ STATIC_URL }}js/csrf.js"></script>
        <script type="text/javascript" src="{{ STATIC_URL }}js/content.js"></script>
        {% endif %}
{% endblock head_js %}

{% block contents %}
{% include 'content/control_panel.html' %}
      <h1>{{ content.instance.name }}</h1>
        <div id="show_content" class="content">
            {{ version.description|safe }}
        </div>
{% endblock contents %}
```

```
#html
{% extends 'base.html' %}

{% block head_css %}
        {{ block.super }}
        {% if user.is_staff %}
        <link rel="stylesheet" type="text/css" href="{{ STATIC_URL }}css/content.css"/>
        {% endif %}
{% endblock head_css %}

{% block head_js %}
        {{ block.super }}
        {% if user.is_staff %}
        <script type="text/javascript" src="{{ STATIC_URL }}js/csrf.js"></script>
        {% include 'content/editor_header.html' %}
        <script type="text/javascript" src="{{ STATIC_URL }}admin/js/urlify.js"></script> {# TODO: refactor in to a shared template which still exposed a hook or customize from the editor #}
        <script type="text/javascript" src="{{ STATIC_URL }}js/content.js"></script>
        <script type="text/javascript">
            content.content.id = '{{ content.instance.id }}';
            {% if edit == True %}content.edit = true;{% endif %}
            $(document).ready(function() {
                content.upload_photos_url = '{% url 'drift_upload_photos' %}';
                content.recent_photos_url = '{% url 'drift_recent_photos' %}';
                content.prepopulated_fields = {{ content.get_perpopulated_fields }};
                content.initialize();
            });
        </script>
        {% endif %}
{% endblock head_js %}

{% block contents %}
<form method="post">
    {% csrf_token %}
    {% include 'content/control_panel.html' %}

    <h1>{{ content.form.name }}</h1>

    <div class="well content_settings">
        <h2><i class="fa fa-cog"></i> Content Settings</h2>
        {% for field in content.form.non_contenteditable_fields %}
        {% with field.field as field %}
        {% include "_field.html" %}
        {% endwith %}
        {% endfor %}
    </div>

    <textarea class="content" name="content">
        {{ content.form.description }}
    </textarea>
  </form>
{% endblock %}
```

# Url hookup

You need to include your foo/urls.py in your site urls.py.

Once this is done you should be able to sign in, go to the url you hooked up, and use the header to create a new Foo object. You can see you list of Foo objects and edit them. The pre-populate for the slug should also work.
