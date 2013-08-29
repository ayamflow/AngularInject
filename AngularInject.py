import sublime
import sublime_plugin


class AngularInjectCommand(sublime_plugin.TextCommand):
  # RegEx variables
    moduleRegEx = "(controller\(|factory\(|service\(|provider\(|directive\(|filter\(|config\(|run\()"
    injectRegEx = "\[\s*.+,\s*function\s*\(.+\)"
    functionRegEx = "\[\s*function\s*\("
    iFunctionRegEx = ",\s*function"
    parenthesisRegEx = "\s*\)"

    def run(self, edit):
        self.view.window().show_input_panel("Dependency name:", '', self.on_done, None, None)

    def on_done(self, value):
        view = self.view.window().active_view()

        # save the requested injection
        self.requestedInjection = value

        # find all modules in the file
        self.modules_regions = view.find_all(self.moduleRegEx)

        # if multiple modules : show the list
        if len(self.modules_regions) > 1:
            modules_list = []
            for region in self.modules_regions:
                start = region.begin()
                end = region.end() + 20
                nRegion = sublime.Region(start, end)
                modules_list.append(view.substr(nRegion) + "...")

            sublime.active_window().show_quick_panel(modules_list, self.on_choice)

        # else inject
        else:
            self.inject(self.modules_regions[0])

    # inject the chosen module, in a multiple modules file
    def on_choice(self, value):
        if value > -1:
            region = self.modules_regions[value]
            self.inject(region)

    def inject(self, region):
        start_point = region.end()
        view = self.view.window().active_view()

        result_region = view.find(self.injectRegEx, start_point)

        # If we already have a dependency in this module...
        if result_region:
            prev_dependancies = view.substr(result_region)

            # Check if the new dependacy isn't already there
            if self.requestedInjection in prev_dependancies:
                sublime.status_message(self.requestedInjection + " Dependency is already injected.")
                return

            # find the ", function" in result_region
            function_region = view.find(self.iFunctionRegEx, result_region.begin())
            # find the last ")" in result_region
            parenthesis_region = view.find(self.parenthesisRegEx, result_region.begin())

            # if both regexp match, replace them to add the new dependacy
            if not function_region.empty() and not parenthesis_region.empty():
                # create write access
                edit = view.begin_edit()
                # inject the dependency (finally !)
                view.replace(edit, parenthesis_region, ", " + self.requestedInjection + ")")
                view.replace(edit, function_region, ", '" + self.requestedInjection + "', function")
                # notify the user
                sublime.status_message("Injected AngularJS Dependency: " + self.requestedInjection)
                # end file write access
                view.end_edit(edit)
            else:
                # doesn't work ?
                sublime.status_message("Couldn't find where to inject.")

        # If we don't have any dependency, things are much simpler
        else:
            result_region = view.find(self.functionRegEx, start_point)
            prev_dependancies = view.substr(result_region)
            edit = view.begin_edit()
            view.replace(edit, result_region, "[ '" + self.requestedInjection + "', function(" + self.requestedInjection)


    # TODO LIST
    #
    # enable inject with other methods ( like $controller.inject([...]) )
