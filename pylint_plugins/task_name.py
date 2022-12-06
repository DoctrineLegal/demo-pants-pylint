from pylint import checkers, interfaces


class FlowObjectNameChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker

    name = "invalid-flow-object-definition-name"

    msgs = {
        "C9002": (
            "The task name is not suffixed by `_task`",
            "invalid-task-definition-name",
            "Emitted when a flow function definition is not suffixed by `_task` as per the naming convention requires",
        ),
    }

    def visit_functiondef(self, node):
        if not node.decorators:
            return

        for decorator in node.decorators.get_children():
            if not hasattr(decorator, "func") or not decorator.func:
                return

            try:
                decorator_name = decorator.func.attrname
            except AttributeError:
                decorator_name = decorator.func.name

            # Is it a `prefect.task` decorator
            if decorator_name == "task":

                if not node.name.endswith("_task"):
                    self.add_message("invalid-task-definition-name", node=node)


def register(linter):
    linter.register_checker(FlowObjectNameChecker(linter))
