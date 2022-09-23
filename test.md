<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style># Test file

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##test.**my_func**

<p class="func-header">
    <i>def</i> test.<b>my_func</b>(<i>param0, param1=1.0</i>) 
</p>

This is my function.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>param0 : <i>str</i></b>
<p class="attr">
    This is parameter 0.
</p>
<b>param1 : <i>float, default=1.0</i></b>
<p class="attr">
    This is parameter 1.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>None : <i></i></b>
<p class="attr">
    
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
my_func('hello', 'world')
```

Out:

```
hello world
```

##test.**MyClass**

<p class="func-header">
    <i>class</i> test.<b>MyClass</b>(<i>param0, param1=None</i>) 
</p>

This is my class.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>param0 : <i>str</i></b>
<p class="attr">
    This is parameter 0.
</p>
<b>param1 : <i>str or None, default=None</i></b>
<p class="attr">
    This is parameter 1.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Attributes:</b></td>
    <td class="field-body" width="100%"><b>attr0 : <i>str</i></b>
<p class="attr">
    This is attribute 0.
</p>
<b>attr1 : <i>str or None</i></b>
<p class="attr">
    This is attribute 1.
</p></td>
</tr>
    </tbody>
</table>

####Notes

This is a note.

####Examples

```python
x = MyClass('param0')
x.print_greeting()
```

Out:

```
hello world
```

####Methods



<p class="func-header">
    <i></i> <b>print_greeting</b>(<i>self, name='world'</i>) 
</p>

This method returns a greeting.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>name : <i>str</i></b>
<p class="attr">
    This is the name of the person to greet.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>greeting : <i>str</i></b>
<p class="attr">
    Of the form 'hello, {name}!'.
</p></td>
</tr>
    </tbody>
</table>

