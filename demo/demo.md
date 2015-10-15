### Introduction

This is a demo for [Backdoc](https://github.com/chibisov/backdoc) - tool for backbone-like documentation generation.

When working on a web application that involves a lot of JavaScript, one of the first things you learn is to stop tying your data to the DOM. It's all too easy to create JavaScript applications that end up as tangled piles of jQuery selectors and callbacks, all trying frantically to keep data in sync between the HTML UI, your JavaScript logic, and the database on your server. For rich client-side applications, a more structured approach is often helpful.

### Events

__Events__ is a module that can be mixed in to any object, giving the object the ability to bind and trigger custom named events. Events do not have to be declared before they are bound, and may take passed arguments. For example:

    var object = {};

    _.extend(object, Backbone.Events);

    object.on("alert", function(msg) {
      alert("Triggered " + msg);
    });

    object.trigger("alert", "an event");

#### on

Bind a callback function to an object. The callback will be invoked whenever the event is fired. If you have a large number of different events on a page, the convention is to use colons to namespace them: `"poll:start"`, or `"change:selection"`. The event string may also be a space-delimited list of several events...

    book.on("change:title change:author", ...);

#### off

Note that calling `model.off()`, for example, will indeed remove all events on the model — including events that Backbone uses for internal bookkeeping.

#### trigger
Trigger callbacks for the given __event__, or space-delimited list of events. Subsequent arguments to __trigger__ will be passed along to the event callbacks.

#### once
Just like [on](#on), but causes the bound callback to only fire once before being removed. Handy for saying "the next time that X happens, do this".

#### Catalog of Events

Here's the complete list of built-in Backbone events, with arguments.

* __"add"__ (model, collection, options) — when a model is added to a collection.
* __"remove"__ (model, collection, options) — when a model is removed from a collection.
* __"reset"__ (collection, options) — when the collection's entire contents have been replaced.
* __"sort"__ (collection, options) — when the collection has been re-sorted.


### Model

__Models__ are the heart of any JavaScript application, containing the interactive data as well as a large part of the logic surrounding it: conversions, validations, computed properties, and access control. You extend __Backbone.Model__ with your domain-specific methods, and __Model__ provides a basic set of functionality for managing changes.

#### extend

To create a __Model__ class of your own, you extend __Backbone.Model__ and provide instance __properties__, as well as optional __classProperties__ to be attached directly to the constructor function.

_Brief aside on `super`: JavaScript does not provide a simple way to call super — the function of the same name defined higher on the prototype chain. If you override a core function like set, or save, and you want to invoke the parent object's implementation, you'll have to explicitly call it, along these lines:_

    var Note = Backbone.Model.extend({
      set: function(attributes, options) {
        Backbone.Model.prototype.set.apply(this, arguments);
        ...
      }
    });

#### constructor / initialize

When creating an instance of a model, you can pass in the initial values of the __attributes__, which will be set on the model. If you define an __initialize__ function, it will be invoked when the model is created. Init could be called with `one.two.three.four.five.six.seven.eight.nine.ten.eleven`

### Responsive Images

![1200x800](./1200x800.png)   
![240x160](./240x160.png)   

### Change Log

__1.1.0__ — _Oct. 10, 2013_

* Made the return values of Collection's `set`, `add`, `remove`, and `reset` more useful. Instead of returning `this`, they now return the changed (added, removed or updated) model or list of models:
    * **List** inside list 1
    * **List** inside list 2
* Backbone Views no longer automatically attach options passed to the constructor as `this.options`, but you can do it yourself if you prefer.

__1.0.0__ — _March 20, 2013_

* The routes in a Router's route map may now be function literals, instead of references to methods, if you like.
* Your route handlers will now receive their URL parameters pre-decoded.
* Added listenToOnce as the analogue of once.
