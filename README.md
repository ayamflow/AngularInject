Sublime Text 2 Plugin : AngularInject
=============

Convenient Sublime Text 2 Plugin to quickly inject a dependency into any AngularJS module

##Installation
### With Package Control:
Just search for AngularInject package and confirm. Tada !
### Manually:
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

If multiple modules exist on the same file, you will be ask to chose the one to inject.

##Next Step
###Know issues
A lot ?
###Todo
1. Allow to remove an injection from the module
2. Make the plugin work with no min-safe version (`MyCtrl.$inject[…]` or `controller('MyCtrl', function()…`)3. inject)
3. Insure that the modified line is really the [ function() from the module

##Contributing
Feel free to modify, share, comment any bug or fork. Just [drop a tweet](http://twitter.com/ayamflow) if you do !