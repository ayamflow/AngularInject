Sublime Text 2 Plugin : AngularInject
=============

Convenient Sublime Text 2 Plugin to quickly inject a dependency into any AngularJS module

##Installation
Only manual installation for now.
Download and extract into your ST2 Packages folder. That's it.
This directory can be found on Mac OS at `~/Library/Application Support/Sublime Text 2/Packages/`

##Usage

####Note: this plugin only work (yet) with inline annotation. It doesn't work (yet) with static injection (example: `MyController.$inject = ['$scope', 'greeter'];`).<br /><br />

By default the plugin can be called with `Cmd + Alt + i` (Mac OS) and `Ctrl + Alt + i` (Windows & Linux).
You can also use the Command Palette to find `AngularJS: Inject Dependency` (any word should work).

You should see the quick panel (bottom of ST2 screen).
Just type in the dependency you wish (for instance $window). Shazam !

Your module should looks like this :

`angular.module('myApp.controllers', []).controller('MyCtrl', [ '$http', function($http) { ... }`

and to something like this after the plugin action (notice the $window injection)

`angular.module('myApp.controllers', []).controller('MyCtrl', [ '$http', '$window', function($http, $window) { ... }`

It is (for now) designed for one module per file so if you have multiples modules (like controllers) in the same file, only the first one will be targeted by this plugin.

##Next Step
###Know issues
A lot ?
###Todo
1. If multiple modules in the same file, enable to chose which one to inject
2. Allow to remove an injection from the module
3. Make the plugin work if no injection exists

##Contributing
Feel free to modify, share, comment any bug or fork. Just [drop a tweet](http://twitter.com/ayamflow) if you do !