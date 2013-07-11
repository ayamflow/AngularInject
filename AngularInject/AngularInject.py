import sublime, sublime_plugin

class AngularInjectCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    self.view.window().show_input_panel("Dependency name:", '', self.on_done, None, None)
  def on_done(self, value):
    view = self.view.window().active_view()
    top_point = self.view.text_point(0, 0)

    start_point = view.find("(controller\(|factory\(|directive\(|filter\(|config\(|run\()", top_point).begin()
    result_region = view.find("\[.+,\s*function\(.+\)", start_point)
    prev_dependancies = view.substr(result_region)
    # print prev_dependancies

    # Check if the new dependacy isn't already there
    if value in prev_dependancies:
        sublime.status_message(value + " Dependency is already injected.")
        return false

    # find the ", function" in result_region
    function_region = view.find(",\s*function", result_region.begin())
    # find the last ")" in result_region
    parenthesis_region = view.find("\s*\)", result_region.begin())

    # if both regexp match, replace them to add the new dependacy
    if not function_region.empty() and not parenthesis_region.empty():
        # create write access
        edit = view.begin_edit()
        # inject the dependency (finally !)
        view.replace(edit, parenthesis_region, ", " + value + ")")
        view.replace(edit, function_region, ", '" + value + "', function")
        # notify the user
        sublime.status_message("Injected AngularJS Dependency: " + value)
        # end file write access
        view.end_edit(edit)
    else:
        # doesn't work ?
        sublime.status_message("Couldn't find where to inject.")



# TODO LIST
#
# test that result_region starts with angular.module
# if more than one angular.module, show a list of all of them, so the user chooses the one he wants to inject
# enable inject with other methods ( like $controller.inject([...]) )
#
#